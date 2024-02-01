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

def creer_armee_ennemie(somme_totale, somme_utilisee):
    fantassin_prix = 150
    archer_prix = 200
    cavalier_prix = 250

    max_fantassins = (somme_totale - somme_utilisee) // fantassin_prix
    max_archers = (somme_totale - somme_utilisee) // archer_prix
    max_cavaliers = (somme_totale - somme_utilisee) // cavalier_prix

    return max_fantassins, max_archers, max_cavaliers

def acheter_unite_ennemie(max_unites):
    # Choix aléatoire du nombre d'unités à acheter
    n_unites = random.randint(0, max_unites)

    return n_unites, n_unites * 100  # Supposons que le coût par unité soit toujours 100 pièces d'or

# Saisie de la somme totale aléatoire pour l'armée
somme_totale = random.randint(500, 1000)
somme_disponible = somme_totale
somme_utilisee = 0
print(f"Somme totale allouée à l'armée : {somme_totale}")

# Création de l'armée en fonction de la somme
max_fantassins, _, _ = creer_armee(somme_totale, somme_utilisee)  # Utiliser les underscores pour ignorer les valeurs non nécessaires

# Achat successif de chaque type d'unité pour l'armée
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

# Saisie de la somme totale aléatoire pour l'armée ennemie
somme_totale_ennemie = somme_totale
somme_disponible_ennemie = somme_totale_ennemie
somme_utilisee_ennemie = 0
print(f"\nSomme totale allouée à l'armée ennemie : {somme_totale_ennemie}")

# Création de l'armée ennemie en fonction de la somme
max_fantassins_ennemie, max_archers_ennemie, max_cavaliers_ennemie = creer_armee_ennemie(somme_totale_ennemie, somme_utilisee_ennemie)

# Achat successif de chaque type d'unité pour l'armée ennemie
n_fantassins_ennemie, cout_fantassins_ennemie = acheter_unite_ennemie(max_fantassins_ennemie)
somme_disponible_ennemie -= cout_fantassins_ennemie
somme_utilisee_ennemie += cout_fantassins_ennemie

# Recalculer les maximaux pour les archers ennemis
max_archers_ennemie, _, _ = creer_armee_ennemie(somme_totale_ennemie, somme_utilisee_ennemie)

n_archers_ennemie, cout_archers_ennemie = acheter_unite_ennemie(max_archers_ennemie)
somme_disponible_ennemie -= cout_archers_ennemie
somme_utilisee_ennemie += cout_archers_ennemie

# Utilisation de max_cavaliers_ennemie pour le dernier achat
max_cavaliers_ennemie, _, _ = creer_armee_ennemie(somme_totale_ennemie, somme_utilisee_ennemie)

n_cavaliers_ennemie, cout_cavaliers_ennemie = acheter_unite_ennemie(max_cavaliers_ennemie)
somme_disponible_ennemie -= cout_cavaliers_ennemie
somme_utilisee_ennemie += cout_cavaliers_ennemie

# Affichage du résumé de l'armée ennemie créée
print("\nRésumé de l'armée ennemie créée :")
print(f"Nombre de Fantassins ennemis ({cout_fantassins_ennemie} pièces) : {n_fantassins_ennemie}")
print(f"Nombre d'Archers ennemis ({cout_archers_ennemie} pièces) : {n_archers_ennemie}")
print(f"Nombre de Cavaliers ennemis ({cout_cavaliers_ennemie} pièces) : {n_cavaliers_ennemie}")

# Calcul du coût total de l'armée ennemie
cout_total_ennemie = cout_fantassins_ennemie + cout_archers_ennemie + cout_cavaliers_ennemie
print(f"Coût total de l'armée ennemie : {cout_total_ennemie} pièces d'or")
