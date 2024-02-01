class Personnage:
    def __init__(self, nom, attaque, defense):
        self.nom = nom
        self.attaque = attaque
        self.defense = defense
        self.points_de_vie = 100

    def combat(self, cible):
        degats_infliges = max(0, self.attaque - cible.defense)
        cible.points_de_vie -= degats_infliges

        print(f"{self.nom} inflige {degats_infliges} points de dégâts à {cible.nom}.")
        print(f"{cible.nom} a maintenant {cible.points_de_vie} points de vie.")

# Création de personnages
joueur1 = Personnage('Joueur 1', 20, 10)
ennemi = Personnage('Ennemi', 15, 5)

# Combat
joueur1.combat(ennemi)
