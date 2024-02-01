from itertools import permutations

# import villes
# from villes import schoelcher
from villes import *

# Utilisez la variable schoelcher dans votre programme principal
# print(SCHOELCHER)
# print(villes.SCHOELCHER)

# Liste des villes du dictionnaire, QUE L ON SOUHAITE TRAITER
noms_villes = ["ROBERT", "SCHOELCHER", "SAINT_PIERRE", "LAMENTIN", "CASE_PILOTE", "FRANCOIS", "SAINTE_MARIE"]

# Liste des itineraires
itineraires = []

# Distances de chaque ville
for nom_depart in noms_villes:
    # Obtenez le dictionnaire correspondant à partir du nom du module
    if nom_depart in VILLES:
        ville_depart = VILLES[nom_depart]
        # Distance des autres villes
        for nom_arrivee, distance in ville_depart.items():
            # Vérification pour éviter de créer des itineraires identiques
            # Pratiquement inutile, mais verif de plus
            if nom_arrivee != nom_depart and isinstance(distance, (int, float)):
                itineraire_trie = sorted([nom_depart.lower(), nom_arrivee])
                itineraires.append([itineraire_trie, distance])
    else:
        print(f"La ville {nom_depart} n'existe pas.")
        
# # Affichage des itineraires
# print("----- itineraires avec doublons -----")
# # print(itineraires)
# for elem in itineraires:    
#     print(*elem)
#     # print(elem)


# ------------------------------------------- Nouvelle liste sans doublons
# Ensemble pour stocker des éléments uniques
itineraires_uniques = set()

# Nouvelle liste sans doublons
itineraires_sans_doublons = []

# Ajouter chaque élément unique à l'ensemble et à la nouvelle liste
for elem in itineraires:
    # Trier les noms de villes pour garantir l'unicité (indépendamment de l'ordre)
    elem_trie = tuple(sorted(elem[0])) + (elem[1],)
    if elem_trie not in itineraires_uniques:
        itineraires_uniques.add(elem_trie)
        if elem not in itineraires_sans_doublons:
            itineraires_sans_doublons.append(elem)

# Affichage de la nouvelle liste sans doublons
# print("----- itineraires sans doublons -----")
# print(itineraires_sans_doublons)
# for elem in itineraires_sans_doublons:
#     print(*elem)
    # print(elem)
    
# Trions la liste par le premier élément de chaque sous-liste (ordre alphabétique)

itineraires_sans_doublons_tries = sorted(itineraires_sans_doublons, key=lambda x: x[0][0].lower())

# print("----- itineraires triés alphabetiquement -----")
# # Affichez la liste triée
# # print(itineraires_sans_doublons_tries)
# for elem in itineraires_sans_doublons_tries:
#     print(*elem)
#     # print(elem)
    
# On re check les doublons

# Ensemble pour suivre les éléments déjà rencontrés
itineraires_deja_rencontres = set()

# Liste sans doublons
itineraires_sans_doublons = []

# Parcourez la liste triée
for elem in itineraires_sans_doublons_tries:
    # Convertissez la sous-liste en tuple pour pouvoir le vérifier dans l'ensemble
    elem_tuple = tuple(elem[0])
    
    # Vérifiez si l'élément est déjà rencontré
    if elem_tuple not in itineraires_deja_rencontres:
        # Ajoutez l'élément à la liste sans doublons
        itineraires_sans_doublons.append(elem)
        
        # Ajoutez l'élément à l'ensemble
        itineraires_deja_rencontres.add(elem_tuple)

# Affichez la liste sans doublons
print("----- itineraires sans doublons -----")
# print(itineraires_sans_doublons)
for elem in itineraires_sans_doublons:
    print(*elem)
    # print(elem)
    
    
###############################

from itertools import permutations

# Ville de départ
ville_depart = "SCHOELCHER"

# Initialiser la somme minimale avec une valeur très grande
somme_minimale = float('inf')

# Parcourir toutes les permutations des villes
for permutation in permutations(noms_villes):
    # Assurez-vous que chaque permutation commence par la ville de départ
    if permutation[0] == ville_depart:
        # Initialiser la somme des distances pour cette permutation
        somme_distances = 0
        # Liste pour stocker les détails de l'itinéraire
        itineraire_details = []

        # Calculer la somme des distances pour chaque étape de la permutation
        # Calculer la somme des distances pour chaque étape de la permutation
        for i in range(len(permutation) - 1):
            # Recherchez la distance entre les villes actuelle et suivante
            distance = next((elem[1] for elem in itineraires_sans_doublons if set(map(str.lower, permutation[i:i+2])) == set(map(str.lower, elem[0]))), None)
            # Si la distance est trouvée, ajoutez-la à la somme
            if distance is not None:
                somme_distances += distance
                itineraire_details.append((permutation[i], permutation[i+1], distance))
                print(f"Étape {i+1}: Ajout de la distance {distance}, Somme actuelle : {somme_distances}")
            else:
                # Si la distance n'est pas trouvée, cette permutation n'est pas valide, passez à la suivante
                break


        # Si la somme des distances pour cette permutation est plus petite que la somme minimale actuelle, mettez à jour la somme minimale
        if somme_distances < somme_minimale:
            somme_minimale = somme_distances
            itineraire_minimal = itineraire_details

# Afficher la somme minimale des distances et les détails de l'itinéraire minimal
print(f"La somme minimale des distances en partant de {ville_depart} en passant une fois par chaque ville est : {somme_minimale}")
print("Détails de l'itinéraire minimal:")
for elem in itineraire_minimal:
    print(f"{elem[0]} -> {elem[1]} : {elem[2]}")
