def creer_personnage(nom, attaque, defense):
    personnage = {
        'nom': nom,
        'attaque': attaque,
        'defense': defense,
        'points_de_vie': 100  # Ajout de l'attribut points_de_vie
    }
    return personnage

def combat(personnage1, personnage2):
    degats1 = max(0, personnage1['attaque'] - personnage2['defense'])
    degats2 = max(0, personnage2['attaque'] - personnage1['defense'])

    personnage1['points_de_vie'] -= degats2
    personnage2['points_de_vie'] -= degats1

    print(f"{personnage1['nom']} inflige {degats1} points de dégâts à {personnage2['nom']}.")
    print(f"{personnage2['nom']} inflige {degats2} points de dégâts à {personnage1['nom']}.")

# Création de personnages
joueur1 = creer_personnage('Joueur 1', 20, 10)
ennemi = creer_personnage('Ennemi', 15, 5)

# Combat
combat(joueur1, ennemi)
