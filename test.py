import random

# Définition de la classe "Fruits"
class Fruits:
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur

# Liste des noms de fruits et des couleurs
noms_fruits = ["coro", "kiwi", "ananas", "pomme", "banane", "orange", "fraise", "raisin", "mangue", "poire"]
couleurs = ["vert", "noir", "rouge", "jaune", "orange", "violet"]
number = 4 # max not sup as len couleurs

# Création d'une liste d'instances de la classe "Fruits"
liste_fruits = [Fruits(nom, couleur) for nom, couleur in zip(noms_fruits, couleurs)]

# Sélection aléatoire de 5 paires de fruits/couleurs
paires_aleatoires = random.sample(list(zip(noms_fruits, couleurs)), number)

# Création de variables pour chaque paire et affichage
for i, (nom, couleur) in enumerate(paires_aleatoires, 1):
    locals()[f"fruit{i}"] = Fruits(nom, couleur)
    print(f"Nom {i}: {locals()[f'fruit{i}'].nom}, Couleur {i}: {locals()[f'fruit{i}'].couleur}")

# Les variables fruit1, fruit2, ..., fruit5 ont été créées avec les paires aléatoires
print(fruit1.nom)
