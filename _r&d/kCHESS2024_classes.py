# kCHESS2024_classes.py

class ECHIQUIER:
    def __init__(self):
        
        self.cases = [
            'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
            'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
            'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5', 'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
            'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7', 'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'
        ]
        
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

    def afficher_echiquier(self, flip=False):
        if flip:
            echiquier_affiche = [row[::-1] for row in self.echiquier_unicode[::-1]]
        else:
            echiquier_affiche = self.echiquier_unicode

        for ligne in echiquier_affiche:
            print(' '.join(ligne))
        print()

    def coordonnees_en_indices(self, coordonnee):
        colonne = ord(coordonnee[0].lower()) - ord('a')
        ligne = 8 - int(coordonnee[1])
        return ligne, colonne

    def check_case_piece(self, choix):
        try:
            ligne, colonne = self.coordonnees_en_indices(choix)
            piece = self.echiquier_unicode[ligne][colonne]
            print(f"La pièce à {choix} est : {piece}")
        except (IndexError, ValueError):
            print("Case invalide.")

    def check_case(self, choix):
        if choix in self.cases:
            return True
        else:
            print(f"Case {choix} invalide.")
            return False