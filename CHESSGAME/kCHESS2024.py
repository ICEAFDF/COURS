# -*- coding : utf8 -*-
"""Jeu d'Echecs v0.5"""

# import os,sys,keyboard,time,subprocess
import os
from datetime import datetime

# from kCHESS2024_classes import ECHIQUIER, Coup, Pion, Tour, Cavalier, Fou, Reine, Roi
from kCHESS2024_classes import *

# Initial setup
ECHIQUIER = ECHIQUIER()
partie_en_cours = ECHIQUIER.partie_en_cours
cases = ECHIQUIER.cases
echiquier = ECHIQUIER.echiquier
pieces_dict = ECHIQUIER.pieces_dict
echiquier_unicode = ECHIQUIER.echiquier_unicode
pieces_mapping = ECHIQUIER.pieces_mapping

# paths
# chemin absolu du fichier Python en cours d'exécution
chemin_script = os.path.abspath(__file__)

# répertoire parent du fichier en cours d'exécution
repertoire_parent = os.path.dirname(chemin_script)

# chemin complet pour le dossier "parties"
chemin_parties = os.path.join(repertoire_parent, 'parties')

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    # une pause pour permettre à la console de se rafraîchir
    # time.sleep(0.5)  

# def clear_console():
#     # subprocess.run(['clear'])  # Pour Linux/Mac
#     subprocess.run(['cls'], shell=True)  # Pour Windows 
#     time.sleep(0.5)

def demander_sauvegarde():
    while True:
        reponse = input("Voulez-vous sauvegarder la partie ? (o/n): ").lower()
        if reponse in ['o', 'n']:
            return reponse

def sauvegarder_partie_pgn(partie_en_cours, nom_fichier):
    # chemin complet du dossier "parties"
    if not os.path.exists(chemin_parties):
        os.makedirs(chemin_parties)

    with open(nom_fichier, 'w') as fichier:
        pgn = format_partie_en_cours_pgn(partie_en_cours)
        fichier.write(pgn)
    print(f"Partie sauvegardée dans {nom_fichier}")

def couleur_piece(position):
    ligne = 8 - int(position[1])
    colonne = ord(position[0]) - ord('a')
    piece = echiquier[ligne][colonne]

    if piece.isupper():
        return 'B'  # Pièce blanche
    elif piece.islower():
        return 'N'  # Pièce noire
    else:
        return ' '  # Case vide

def valeur_piece(position):
    ligne = 8 - int(position[1])
    colonne = ord(position[0]) - ord('a')
    return echiquier[ligne][colonne]

def format_partie_en_cours(partie_en_cours):
    formatted_moves = [f"{coup.piece.__class__.__name__} {coup.couleur}: {coup.start}-{coup.end}" for coup in partie_en_cours]
    return "\n".join(formatted_moves)

def format_partie_en_cours_pgn(partie_en_cours):
    moves_pgn = []
    for i, coup in enumerate(partie_en_cours, start=1):
        move = f"{i}. {coup.start[0]}{coup.start[1]}-{coup.end[0]}{coup.end[1]}"
        moves_pgn.append(move)
    return ' '.join(moves_pgn)

def choisir_couleurs():
    while True:
        couleur_joueur_blanc = input("Couleur (B ou N), 'q' pour quitter : ").upper()
        
        if couleur_joueur_blanc == 'Q':
            print("Au revoir !")
            exit()  # Quitter le programme si 'q' est entré
        
        if couleur_joueur_blanc in ['B', 'N']:
            couleur_joueur_noir = 'B' if couleur_joueur_blanc == 'N' else 'N'
            return couleur_joueur_blanc, couleur_joueur_noir
        else:
            print("Veuillez saisir une couleur valide (B ou N).")

def est_case_valide(coordonnee):
    """
    Vérifie si la coordonnée est valide (par exemple, 'a1', 'h8').
    """
    if len(coordonnee) != 2:
        return False

    colonne, ligne = coordonnee[0], coordonnee[1]

    if not ('a' <= colonne <= 'h' and '1' <= ligne <= '8'):
        return False

    return True


def validation_input(input_sequence, partie_en_cours, couleur_attendue):
    # Séparer les coordonnées de départ et d'arrivée
    start, end = input_sequence.split('-')

    # Vérifier si les coordonnées sont valides
    if not (est_case_valide(start) and est_case_valide(end)):
        print("Coordonnées invalides. Veuillez entrer un coup au format 'a2-a4'.")
        return False

    # Vérifier si la case de départ contient une pièce de la bonne couleur
    piece_present = partie_en_cours.get_piece(start)
    if piece_present is None or piece_present.couleur != couleur_attendue:
        print("Case de départ invalide. Veuillez sélectionner une pièce de votre couleur.")
        return False

    # Vérifier si le mouvement est autorisé pour la pièce
    if not piece_present.check_bouger_piece(start, end, piece_present):
        print("Mouvement invalide pour la pièce sélectionnée.")
        return False

    # Vérifier si le chemin entre la case de départ et d'arrivée est dégagé
    if not est_chemin_degagé(partie_en_cours, start, end):
        print("Le chemin entre la case de départ et d'arrivée n'est pas dégagé.")
        return False

    # Vérifier si le roi serait en échec après le mouvement
    if est_roi_en_echec_apres_mouvement(partie_en_cours, start, end, couleur_attendue):
        print("Le roi serait en échec après ce mouvement.")
        return False

    return True



def nouvelle_partie():
    couleur_joueur_blanc, couleur_joueur_noir = choisir_couleurs()

    # Initialisation de joueur_courant au lieu de couleur_attendue
    joueur_courant = couleur_joueur_blanc

    while True:
        clear_console()
        partie_en_cours = ECHIQUIER.partie_en_cours

        print("")
        if couleur_joueur_blanc == 'B':
            ECHIQUIER.print_echiquier_unicode()
        else:
            ECHIQUIER.print_echiquier_unicode_noirs()

        if partie_en_cours:
            print('')
            print(format_partie_en_cours_pgn(partie_en_cours))
            print("")

        if 'validation_result' in locals() and validation_result:
            print(f"Coup invalide : {validation_result}")
            del validation_result
        else:
            print('')

        if joueur_courant == couleur_joueur_blanc:
            couleur_attendue = couleur_joueur_blanc
        else:
            couleur_attendue = couleur_joueur_noir

        input_sequence = input(f"Entrez coup pour les {couleur_attendue} (ex. a2-a4). 'q' sauvegarder/quitter, 'qq' quitter : ")

        if input_sequence.lower() == 'qq':
            print("Au revoir !")
            break
                
        if input_sequence.lower() == 'q':
            if partie_en_cours:
                sauvegarde_demandee = demander_sauvegarde()
                if sauvegarde_demandee == 'o':
                    date_actuelle = datetime.now().strftime("%Y%m%d_%H%M%S")
                    nom_fichier = input("Entrez le nom du fichier pour sauvegarder la partie (sans extension) : ")
                    nom_complet_fichier_pgn = f"{nom_fichier}-{date_actuelle}.pgn"
                    chemin_fichier_pgn = os.path.join(chemin_parties, nom_complet_fichier_pgn)
                    sauvegarder_partie_pgn(partie_en_cours, chemin_fichier_pgn)
            print("Au revoir !")
            break

        validation_result = validation_input(input_sequence, partie_en_cours, couleur_attendue)

        if joueur_courant == couleur_joueur_blanc:
            joueur_courant = couleur_joueur_noir
        else:
            joueur_courant = couleur_joueur_blanc

        if validation_result is not None:
            continue

    # Message de sortie après la boucle principale
    print("Partie terminée. Merci d'avoir joué !")



# Démarrez une nouvelle partie
nouvelle_partie()