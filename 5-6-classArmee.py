import random

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

def creer_armee(somme_totale, somme_utilisee):
    fantassin_prix = 150
    archer_prix = 200
    cavalier_prix = 250

    max_fantassins = (somme_totale - somme_utilisee) // fantassin_prix
    max_archers = (somme_totale - somme_utilisee) // archer_prix
    max_cavaliers = (somme_totale - somme_utilisee) // cavalier_prix

    return max_fantassins, max_archers, max_cavaliers

def acheter_unite(type_unite, max_unites, somme_disponible):
    cout_unitaire = {'Fantassin': 150, 'Archer': 200, 'Cavalier': 250}[type_unite]
    print(f"Coût d'une unité de {type_unite} : {cout_unitaire} pièces d'or")
    
    while True:
        try:
            n_unites = int(input(f"Entrez le nombre de {type_unite} (maximum {max_unites}, coût par unité : {cout_unitaire}, somme disponible : {somme_disponible}) : "))
            cout_total = n_unites * cout_unitaire
            if 0 <= n_unites <= max_unites and cout_total <= somme_disponible:
                return n_unites, cout_total
            else:
                print("Quantité invalide ou somme insuffisante. Réessayez.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

# Saisie de la somme totale aléatoire
somme_totale = random.randint(500, 1000)
somme_disponible = somme_totale
somme_utilisee = 0
print(f"Somme totale allouée : {somme_totale}")

# Création d'une armée en fonction de la somme
max_fantassins, _, _ = creer_armee(somme_totale, somme_utilisee)  # Utiliser les underscores pour ignorer les valeurs non nécessaires

# Achat successif de chaque type d'unité
n_fantassins, cout_fantassins = acheter_unite('Fantassin', max_fantassins, somme_disponible)
somme_disponible -= cout_fantassins
somme_utilisee += cout_fantassins

# Recalculer les maximaux pour les archers
max_archers, _, _ = creer_armee(somme_totale, somme_utilisee)

n_archers, cout_archers = acheter_unite('Archer', max_archers, somme_disponible)
somme_disponible -= cout_archers
somme_utilisee += cout_archers

# Utilisation de max_cavaliers pour le dernier achat
max_cavaliers, _, _ = creer_armee(somme_totale, somme_utilisee)

n_cavaliers, cout_cavaliers = acheter_unite('Cavalier', max_cavaliers, somme_disponible)
somme_disponible -= cout_cavaliers
somme_utilisee += cout_cavaliers

# Affichage du résumé de l'armée créée
print("\nRésumé de l'armée créée :")
print(f"Nombre de Fantassins ({cout_fantassins} pièces) : {n_fantassins}")
print(f"Nombre d'Archers ({cout_archers} pièces) : {n_archers}")
print(f"Nombre de Cavaliers ({cout_cavaliers} pièces) : {n_cavaliers}")

# Calcul du coût total de l'armée
cout_total = cout_fantassins + cout_archers + cout_cavaliers
print(f"Coût total de l'armée : {cout_total} pièces d'or")
