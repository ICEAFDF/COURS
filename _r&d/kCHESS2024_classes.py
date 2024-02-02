# kCHESS2024_classes.py

class ECHIQUIER:
    def __init__(self):
        self.echiquier_unicode = [
            ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
            ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
        ]

    def afficher_echiquier(self):
        for ligne in self.echiquier_unicode:
            print(' '.join(ligne))
        print()

    def coordonnees_en_indices(self, coordonnee):
        colonne = ord(coordonnee[0].lower()) - ord('a')
        ligne = 8 - int(coordonnee[1])
        return ligne, colonne
    
    def choisir_couleur(self):
        while True:
            couleur = input("Choisissez la couleur (B pour blanc, N pour noir) : ").upper()
            if couleur in ['B', 'N']:
                return couleur
            else:
                print("Choix invalide. Veuillez choisir B pour blanc ou N pour noir.")

    def check_case(self, choix):
        try:
            ligne, colonne = self.coordonnees_en_indices(choix)
            piece = self.echiquier_unicode[ligne][colonne]
            print(f"La pièce à {choix} est : {piece}")
        except (IndexError, ValueError):
            print("Coordonnées invalides. Veuillez entrer des coordonnées correctes.")