# -*- coding: utf8 -*-
"""Jeu d'Echecs v0.6"""

# import os,sys,keyboard,time,subprocess
import os
from datetime import datetime

# from kCHESS2024_classes import ECHIQUIER, Coup, Pion, Tour, Cavalier, Fou, Reine, Roi
from kCHESS2024_classes import *

# Initial setup
ECHIQUIER = ECHIQUIER()
check_case = ECHIQUIER.check_case

liste_coups = []


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
    
def format_partie_en_cours_pgn(partie_en_cours):
    moves_pgn = []
    for i, coup in enumerate(partie_en_cours, start=1):
        move = f"{i}. {coup.start[0]}{coup.start[1]}-{coup.end[0]}{coup.end[1]}"
        moves_pgn.append(move)
    return ' '.join(moves_pgn)

def choisir_couleur():
    while True:
        couleur = input("Choisissez la couleur (B pour blanc, N pour noir) : ").upper()
        if couleur in ['B', 'N']:
            return couleur
        else:
            print("Choix invalide. Veuillez choisir B pour blanc ou N pour noir.")

def validation_input(input_sequence, couleur):
    # Check if the input contains a dash
    if '-' not in input_sequence:
        print("Veuillez entrer un coup valide avec un tiret (-).")
        return False

    # Séparer les coordonnées de départ et d'arrivée
    start, end = input_sequence.split('-')
    
    # Vérifier si les coordonnées de départ et d'arrivée sont valides
    if not check_case(start) or not check_case(end):
        print("Veuillez entrer des coordonnées correctes.")
        return False

    # Autres vérifications ou traitements si nécessaire
    return True



def nouvelle_partie():
    couleur_choisie = choisir_couleur()
    while True:
        # clear_console()
        if couleur_choisie == 'N':
            ECHIQUIER.afficher_echiquier(flip=True)
        else:
            ECHIQUIER.afficher_echiquier()

        input_sequence = input(f"Entrez coup pour les {couleur_choisie} (ex. a2-a4). 'q' sauvegarder/quitter, 'qq' quitter : ")
        
        # Validate the input and proceed accordingly
        if validation_input(input_sequence, couleur_choisie):
            # Autres actions à effectuer si les coordonnées sont valides
            print("Coordonnées valides. Traitement à effectuer.")

        if input_sequence.lower() == 'qq':
            print("Au revoir !")
            break
                
        if input_sequence.lower() == 'q':
            if liste_coups:
                sauvegarde_demandee = demander_sauvegarde()
                if sauvegarde_demandee == 'o':
                    date_actuelle = datetime.now().strftime("%Y%m%d_%H%M%S")
                    nom_fichier = input("Entrez le nom du fichier pour sauvegarder la partie (sans extension) : ")
                    nom_complet_fichier_pgn = f"{nom_fichier}-{date_actuelle}.pgn"
                    chemin_fichier_pgn = os.path.join(chemin_parties, nom_complet_fichier_pgn)
                    sauvegarder_partie_pgn(liste_coups, chemin_fichier_pgn)
            print("Au revoir !")
            break

    # Message de sortie après la boucle principale
    print("Partie terminée. Merci d'avoir joué !")



    


# Démarrez une nouvelle partie
nouvelle_partie()