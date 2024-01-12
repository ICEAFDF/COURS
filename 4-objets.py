# Définition de quelques objets sans utiliser de classe Animal

# Objet Chat
chat = {
    "type": "Terrestre",
    "couleur": "Noir",
    "poids": 4.5,
    "miauler": lambda: print("Miaou!")
}

# Objet Chien
chien = {
    "type": "Terrestre",
    "couleur": "Marron",
    "poids": 12.0,
    "aboyer": lambda: print("Woof!")
}

# Objet Poisson
poisson = {
    "type": "Marin",
    "couleur": "Bleu",
    "poids": 0.3,
    "nager": lambda: print("Nageant dans l'eau")
}

# Accès aux attributs et appels de méthodes
print(f"Couleur du chat : {chat['couleur']}")
print(f"Poids du chien : {chien['poids']} kg")
print(f"Type de poisson : {poisson['type']}")
print(f"Type de poisson : {poisson['nager']}")

# Appels de méthodes
chat['miauler']()
chien['aboyer']()
poisson['nager']()
