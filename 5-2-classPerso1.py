class Guerrier:
    def __init__(self, *args):
        if len(args) == 1 and (isinstance(args[0], tuple) or isinstance(args[0], list)):
            # Si un seul argument est passé et que c'est un tuple ou une liste, 
            # utilisez ses éléments
            type, nom, points_de_vie, attaque, defense, prix = args[0]
        elif len(args) == 6:
            # S'il y a exactement six arguments, prenez-les tels quels
            type, nom, points_de_vie, attaque, defense, prix = args
        else:
            raise ValueError("Nombre incorrect d'arguments")

        self.type = type
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.attaque = attaque
        self.defense = defense
        self.prix = prix

    def attaquer(self, ennemi):
        degats_infliges = self.attaque - ennemi.defense
        ennemi.points_de_vie -= degats_infliges
        print(f"{self.nom} attaque {ennemi.nom} et lui inflige {degats_infliges} points de dégâts.")
        print(f"Prix : {self.prix}")
        print(f"Type : {self.type}")
        print(f"Prix de l'ennemi : {ennemi.prix}")

# Exemple d'utilisation
type_fantassin = ("Fantassin", "Joueur 1", 100, 20, 10, 20)
guerrier1 = Guerrier(type_fantassin)
print(f"Prix du Guerrier 1 : {guerrier1.prix}")

ennemi1 = Guerrier("Fantassin", "Joueur 2", 100, 20, 10, 20)

guerrier1.attaquer(ennemi1)
