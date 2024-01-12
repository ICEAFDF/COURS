import random

# Définir une liste de langues disponibles
langues_disponibles = ["français", "anglais", "espagnol", "chinois", "arabe", "portugais", "russe", "créole", "hindi", "allemand"]

# Créer un dictionnaire de pays avec des langues aléatoires
pays = {}
for nom_pays in ["France", "États-Unis", "Haïti", "Brésil"]:
    if nom_pays == "Haïti":
        langues_pays = ["français", "créole"]
    else:
        langues_pays = random.sample(langues_disponibles, random.randint(1, len(langues_disponibles)))

    pays[nom_pays] = {
        "population": random.randint(5000000, 2000000000),
        "capitale": "Capitale de " + nom_pays,
        "langues": langues_pays,
        "continent": "Continent de " + nom_pays,
        "monnaie": "Monnaie de " + nom_pays
    }

# Afficher les pays
print("Pays :", pays)


pays_creole = [nom_pays for nom_pays, infos in pays.items() if "créole" in infos["langues"]]
print("Pays où l'on parle créole :", pays_creole)

# Supprimer du dictionnaire toutes les langues hors créole et français
for infos in pays.values():
    infos["langues"] = [langue for langue in infos["langues"] if langue in ["français", "créole"]]

# Nouveau dictionnaire avec les pays où l'on parle créole
nouveau_pays_creole = {
    nom_pays: {
        "population": infos["population"],
        "capitale": infos["capitale"],
        "langues": infos["langues"],
        "continent": infos["continent"],
        "monnaie": infos["monnaie"]
    }
    for nom_pays, infos in pays.items() if "créole" in infos["langues"]
}

# Afficher le nouveau dictionnaire
print("\nNouveau dictionnaire avec les pays où l'on parle créole :")
for nom_pays, infos in nouveau_pays_creole.items():
    print(f"\n{nom_pays}:")
    print("  Population:", infos["population"])
    print("  Capitale:", infos["capitale"])
    print("  Langues:", infos["langues"])
    print("  Continent:", infos["continent"])
    print("  Monnaie:", infos["monnaie"])

