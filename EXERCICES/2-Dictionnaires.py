fruits = {
    "pomme": "rouge",
    "Banane": "jaune",
    "orange": "orange",
    "fraise": "rouge",
    "kiwi": "vert",
    "raisin": "violet",
    "ananas": "jaune",
    "mangue": "jaune",
    "poire": "vert",
    "cerise": "rouge"
}

# 1- Afficher tous les fruits avec un 'a'
fruits_avec_a = [fruit for fruit in fruits if 'a' in fruit.lower()]
print("Fruits avec un 'a' :", fruits_avec_a)

# 2- Afficher tous les fruits avec un 'a' et un 'n'
fruits_avec_a_et_n = [fruit for fruit in fruits if 'a' in fruit.lower() and 'n' in fruit.lower()]
print("Fruits avec un 'a' et un 'n' :", fruits_avec_a_et_n)

# 3- Afficher tous les fruits avec un 'a' et un 'B'
fruits_avec_a_et_B = [fruit for fruit in fruits if 'a' in fruit.lower() and 'B' in fruit]
print("Fruits avec un 'a' et un 'B' :", fruits_avec_a_et_B)

# 4- Afficher tous les fruits verts
fruits_verts = [fruit for fruit, couleur in fruits.items() if couleur.lower() == 'vert']
print("Fruits verts :", fruits_verts)

# 5- Afficher tous les fruits rouges avec un 'o'
fruits_rouges_avec_o = [fruit for fruit, couleur in fruits.items() if couleur.lower() == 'rouge' and 'o' in fruit.lower()]
print("Fruits rouges avec un 'o' :", fruits_rouges_avec_o)
