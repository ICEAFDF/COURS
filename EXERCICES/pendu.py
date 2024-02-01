#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Auteurs : Kierian Cousin & Eric Berthomier

import random

# Fonction permettant l'importation d'un fichier et son traitement (suppression des retours chariot)
def traitement_fichier():
    temp = []  # Déclaration d'une liste
    f = open(r"C:\xampp\htdocs\_COURS\ICEA\COURS\EXERCICES\pendu_mots.txt", 'r')  # Assignation d'un fichier à la variable f
    lesLignes = f.readlines()  # La variable prend l'ensemble des lignes du fichier
    for i in lesLignes:  # Boucle sur les lignes
        temp.append(i.replace("\n", ""))  # Chaque ligne s'ajoute à la liste temp
    return temp

def affiche_mot_a_trouver(mot_liste):
    print("Votre jeu : ")
    print("\t" + " ".join(mot_liste))

liste_mots = traitement_fichier()  # Appel de la fonction traitement_fichier()
mot = liste_mots[random.randint(0, len(liste_mots) - 1)]  # Choix d'un mot au hasard dans la liste chaine
user_word = ["_"] * len(mot)  # Mot trouvé par l'utilisateur

find_word = list(mot)  # Le mot est transposé en liste
max_essais = 11
essais = 1
trouve = False

# Affiche le mot à trouver
affiche_mot_a_trouver(user_word)

# Tant que le nombre d'essais n'est pas écoulé et que le mot n'est pas trouvé alors on joue
while essais < 11 and not trouve:
    print()
    print("Essai n° : %d" % essais)
    caractere = input("Veuillez entrer une lettre : ")
    lettre_trouvee = False
    for element in range(len(find_word)):  # Boucle sur le nombre d'éléments de la liste l_mot
        if find_word[element] == caractere:  # Si l'élément de la liste est égal au caractère saisi
            user_word[element] = caractere  # On remplace dans chaine1 "_" par le caractère
            lettre_trouvee = True
    if not lettre_trouvee:
        essais += 1  # On augmente le nombre d'essais uniquement si la personne n'a pas trouvé de lettre
    affiche_mot_a_trouver(user_word)

    if user_word == find_word:  # Si le mot à trouver est égal à la liste l_mot, c'est gagné
        trouve = True

if trouve:
    print("Vous avez gagné, le mot était %s" % (mot))  # Gagné
else:
    print("Vous avez perdu, le mot était %s" % (mot))  # Si c'est différent, c'est perdu
