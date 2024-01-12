class Animal:
    def __init__(self, couleur, poids, terrestre):
        self.couleur = couleur
        self.poids = poids
        self.terrestre = terrestre

    def afficher_details(self):
        print(f"Couleur: {self.couleur}")
        print(f"Poids: {self.poids} kg")
        print(f"Type: {'Terrestre' if self.terrestre else 'Marin'}")

class Chat(Animal):
    def __init__(self, couleur, poids):
        super().__init__(couleur, poids, True)  # Les chats sont terrestres par défaut

    def miauler(self):
        print("Miaou!")

class Chien(Animal):
    def __init__(self, couleur, poids):
        super().__init__(couleur, poids, True)  # Les chiens sont terrestres par défaut

    def aboyer(self):
        print("Woof!")

class Poisson(Animal):
    def __init__(self, couleur, poids):
        super().__init__(couleur, poids, False)  # Les poissons sont marins par défaut

    def nager(self):
        print("Nageant dans l'eau")

# Exemple d'utilisation
mon_chat = Chat(couleur="Noir", poids=4.5)
mon_chien = Chien(couleur="Marron", poids=12.0)
mon_poisson = Poisson(couleur="Bleu", poids=0.3)

mon_chat.afficher_details()
mon_chat.miauler()

print("\n")

mon_chien.afficher_details()
mon_chien.aboyer()

print("\n")

mon_poisson.afficher_details()
mon_poisson.nager()
