from collections import Counter

VILLES = {
    "ROBERT": {
        "lamentin": 15,
        "sainte_marie": 17,
        "francois": 11,
        "case_pilote": 32,
        "saint_pierre": 44,
        "schoelcher": 26,
    },

    "SCHOELCHER": {
        "robert": 26,
        "lamentin": 18,
        "sainte_marie": 42,
        "francois": 28,
        "case_pilote": 7,
        "saint_pierre": 25,
    },

    "SAINT_PIERRE": {
        "robert": 44,
        "lamentin": 40,
        "sainte_marie": 50,
        "francois": 53,
        "case_pilote": 18,
        "schoelcher": 25,
    },

    "LAMENTIN": {
        "robert": 15,
        "sainte_marie": 28,
        "saint_pierre": 40,
        "francois": 14,
        "case_pilote": 21,
        "schoelcher": 18,
    },

    "CASE_PILOTE": {
        "robert": 32,
        "lamentin": 21,
        "sainte_marie": 48,
        "francois": 35,
        "saint_pierre": 18,
        "schoelcher": 7,
    },

    "FRANCOIS": {
        "robert": 11,
        "lamentin": 14,
        "sainte_marie": 28,
        "case_pilote": 35,
        "saint_pierre": 53,
        "schoelcher": 28,
    },

    "SAINTE_MARIE": {
        "robert": 17,
        "lamentin": 28,
        "francois": 28,
        "case_pilote": 48,
        "saint_pierre": 50,
        "schoelcher": 42,
    },
}

# check si distances analogues

# Liste des villes du dictionnaire, QUE L ON SOUHAITE TRAITER
noms_villes = list(VILLES.keys())
villes_dict_list = [VILLES[nom] for nom in noms_villes]


# Liste pour stocker les distances
distances = []

# Parcourir chaque dictionnaire
for nom_dictionnaire, dictionnaire in zip(noms_villes, villes_dict_list):
    for ville, distance in dictionnaire.items():
        depart = nom_dictionnaire.lower()
        arrivee = ville
        etape = sorted([depart, arrivee])
        distances.append(f"{etape[0]}-{etape[1]}-{distance}")


# print(distances)

# on élimine les éléments identiques
# en ne gardant que les elements uniques

# Compter le nombre d'occurrences de chaque élément
compteur = Counter(distances)

# Nouvelle liste pour stocker les éléments uniques qui n'apparaissent qu'une fois
distances_uniques = [elem for elem, count in compteur.items() if count == 1]
distances_uniques = sorted(distances_uniques)

# Afficher le résultat
if distances_uniques:
    print("")
    print("-----------------------------------")
    print("ces paires de villes posent problemes, distances non identiques!")
    print("")
    # print(distances_uniques)
    for elem in distances_uniques:    
        print(elem)
    print("")
    print("-----------------------------------")
    print("")
