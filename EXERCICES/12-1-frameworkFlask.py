from flask import Flask, jsonify

app = Flask(__name__)

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
        return f"{self.nom} attaque {cible.nom} et lui inflige {max(0, degats_infliges)} points de dégâts."

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

@app.route('/')
def hello():
    return "Bienvenue sur l'API de gestion d'armées!"

@app.route('/creer_armee/<int:somme_totale>/<int:somme_utilisee>', methods=['GET'])
def creer_armee_api(somme_totale, somme_utilisee):
    max_fantassins, max_archers, max_cavaliers = creer_armee(somme_totale, somme_utilisee)
    return jsonify({
        'max_fantassins': max_fantassins,
        'max_archers': max_archers,
        'max_cavaliers': max_cavaliers
    })

@app.route('/acheter_unite/<string:type_unite>/<int:max_unites>/<int:somme_disponible>', methods=['GET'])
def acheter_unite_api(type_unite, max_unites, somme_disponible):
    n_unites, cout_total = acheter_unite(type_unite, max_unites, somme_disponible)
    return jsonify({
        'n_unites': n_unites,
        'cout_total': cout_total
    })

if __name__ == '__main__':
    app.run(debug=True)
