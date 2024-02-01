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

def validation_input(input_str, partie_en_cours, couleur_attendue):
    # Check présence du séparateur '-'
    if '-' not in input_str:
        return "La séquence doit contenir le caractère '-' pour spécifier le mouvement."

    # Séparation des cases
    start, end = input_str.split('-')

    # Vérification que les deux cases sont dans la liste
    if start not in cases and end not in cases:
        return "Les deux cases ne sont pas dans la liste."
    elif start not in cases:
        return f"La case {start} n'est pas dans la liste."
    elif end not in cases:
        return f"La case {end} n'est pas dans la liste."

    # Vérifie la parité du coup.
    if len(partie_en_cours) % 2 == 1 and couleur_piece(start) != couleur_attendue:
        return f"Les pièces {couleur_piece(start)} doivent jouer ce coup."
    elif len(partie_en_cours) % 2 == 0 and couleur_piece(start) != couleur_attendue:
        return f"Les pièces {couleur_piece(start)} doivent jouer ce coup."

    valeur_start = valeur_piece(start)

    # On crée une instance de la classe Pion
    pion_instance = Pion(couleur_attendue)

    # Vérifie si le déplacement est autorisé pour le pion.
    if not pion_instance.check_bouger_piece(start, end):
        return "Déplacement de pion non autorisé."

    coup_joue = Coup(start, end, valeur_start, couleur_attendue, ECHIQUIER)
    partie_en_cours.append(coup_joue)

    # Met à jour l'échiquier avec le nouveau coup
    ECHIQUIER.make_move(start, end)

    # échiquier mis à jour
    ECHIQUIER.print_echiquier_unicode()

    return None


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