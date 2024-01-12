import json

# Charger le contenu du fichier JSON dans un dictionnaire
# Solution 1
with open(r'C:\xampp\htdocs\_COURS\ICEA\COURS\EXERCICES\fruits.json', 'r') as file:
    fruits = json.load(file)
    
# Solution 2
# with open('C:\\xampp\\htdocs\\_COURS\\ICEA\\COURS\\EXERCICES\\fruits.json', 'r') as file:
#     fruits = json.load(file)

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
