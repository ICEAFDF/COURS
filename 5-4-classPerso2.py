class Guerrier:
    def __init__(self, nom, points_de_vie, attaque, defense, prix=100, type_guerrier=""):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.attaque = attaque
        self.defense = defense
        self.prix = prix
        self.type_guerrier = type_guerrier

    def attaquer(self, cible):
        degats_infliges = self.attaque - cible.defense
        cible.points_de_vie -= max(0, degats_infliges)
        print(f"{self.nom} attaque {cible.nom} et lui inflige {max(0, degats_infliges)} points de dégâts.")
        print(f"{self.nom} a {self.points_de_vie} points de vie restants.")
        print(f"{cible.nom} a {cible.points_de_vie} points de vie restants.")

class Fantassin(Guerrier):
    def __init__(self, nom):
        super().__init__(nom, points_de_vie=100, attaque=20, defense=10, prix=150, type_guerrier="Fantassin")

class Archer(Guerrier):
    def __init__(self, nom):
        super().__init__(nom, points_de_vie=80, attaque=25, defense=5, prix=200, type_guerrier="Archer")

class Cavalier(Guerrier):
    def __init__(self, nom):
        super().__init__(nom, points_de_vie=120, attaque=15, defense=15, prix=250, type_guerrier="Cavalier")

# Exemples d'utilisation
fantassin1 = Fantassin("Fantassin 1")
archer1 = Archer("Archer 1")
cavalier1 = Cavalier("Cavalier 1")

fantassin1.attaquer(archer1)
archer1.attaquer(cavalier1)
cavalier1.attaquer(fantassin1)
