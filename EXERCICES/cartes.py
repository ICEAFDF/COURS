# Déclaration des listes
cartes=["1","2","3","4","5","6","7","8","9","10","V","D","R"]
couleurs=["Coeur","Pique","Trefle","Carreau"]
jeudecarte1 = []

# Création des jeux de cartes
for type_couleur in couleurs : # Boucle sur les couleurs de la liste couleur
    for element in cartes : # Boucle sur les valeurs de la liste cartes
        carte = element + "_"+ type_couleur # Association d'une couleur avec une valeur
        jeudecarte1.append (carte) # Ajout de la carte à la liste jeude carte1

print (jeudecarte1) # Affichage de la liste jeudecarte1
print(len(jeudecarte1))