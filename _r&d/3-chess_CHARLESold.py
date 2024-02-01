class ECHIQUIER:
    def __init__(self):
        
        self.partie_en_cours = []
        
        # self.cases = [
        #     f"{col}{row}" for row in range(1, 9) for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        # ]

        self.cases = [
            'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4', 'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5', 'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7', 'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'
        ]
        
        self.echiquier_unicode = [
            ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
            ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
            ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        ]
        
        self.pieces_mapping = {
            'P': 'Pion', 'p': 'Pion',
            'T': 'Tour', 't': 'Tour',
            'C': 'Cavalier', 'c': 'Cavalier',
            'F': 'Fou', 'f': 'Fou',
            'D': 'Dame', 'd': 'Dame',
            'R': 'Roi', 'r': 'Roi',
        }
        self.pieces_dict = {
            'P': '♙', 'N': '♘', 'B': '♗', 'R': '♖', 'Q': '♕', 'K': '♔',
            'p': '♟', 'n': '♞', 'b': '♝', 'r': '♜', 'q': '♛', 'k': '♚'
        }
        self.echiquier = [
            ['t', 'c', 'f', 'd', 'r', 'f', 'c', 't'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['T', 'C', 'F', 'D', 'R', 'F', 'C', 'T']
        ]

    def print_echiquier(self):
        for row in self.echiquier:
            print(' '.join(row))
        print()

    def print_echiquier_unicode(self):
        for ligne in range(8):
            for colonne in range(8):
                position = chr(ord('a') + colonne) + str(8 - ligne)
                valeur = self.echiquier[ligne][colonne]
                piece_unicode = self.pieces_dict.get(valeur, valeur)
                print(f"{piece_unicode}", end='  ')
            print()

    def print_echiquier_unicode_with_labels(self):
        for ligne in range(8):
            for colonne in range(8):
                valeur = self.echiquier[ligne][colonne]
                piece_unicode = self.pieces_dict.get(valeur, valeur)
                print(f"{piece_unicode}", end='  ')
            print(f" {8 - ligne}")
        print(" a b c d e f g h")

    def make_move(self, start, end):
        # Add logic to make a move on the ECHIQUIER
        pass

class Pieces:
    def __init__(self, couleur, cases_possibles=None, mouvements_possibles=None):
        self.couleur = couleur
        self.cases_possibles = cases_possibles or []
        self.mouvements_possibles = mouvements_possibles or []

    def __str__(self):
        return f"{self.couleur} {self.__class__.__name__}"

class Pion(Pieces):
    def __init__(self, couleur):
        super().__init__(couleur)

class Tour(Pieces):
    def __init__(self, couleur):
        super().__init__(couleur)

class Cavalier(Pieces):
    def __init__(self, couleur):
        super().__init__(couleur)

class Fou(Pieces):
    def __init__(self, couleur):
        super().__init__(couleur)

class Reine(Pieces):
    def __init__(self, couleur):
        super().__init__(couleur)

class Roi(Pieces):
    def __init__(self, couleur):
        super().__init__(couleur)

class Coup:
    def __init__(self, start, end, piece, couleur):
        self.start = start
        self.end = end
        self.couleur = couleur

        # Si piece est une chaîne, créez une instance de la classe correspondante
        if isinstance(piece, str):
            self.piece = self.creer_instance_piece(piece)
        else:
            self.piece = piece

    def creer_instance_piece(self, piece_str):
        # Utilisez votre mapping pour créer une instance de la classe de pièce appropriée
        piece_key = piece_str.upper()
        if piece_key in pieces_mapping:
            classe_piece = pieces_mapping[piece_key]
            return classe_piece(couleur=self.couleur)
        else:
            raise ValueError(f"Type de pièce inconnu : {piece_str}")
        pass

    def __str__(self):
        return f"{self.piece.couleur} {self.piece.__class__.__name__} de {self.start} à {self.end}"

# Initial setup

ECHIQUIER = ECHIQUIER()
partie_en_cours = ECHIQUIER.partie_en_cours
cases = ECHIQUIER.cases
echiquier = ECHIQUIER.echiquier
pieces_dict = ECHIQUIER.pieces_dict
echiquier_unicode = ECHIQUIER.echiquier_unicode
pieces_mapping = ECHIQUIER.pieces_mapping
# creer_instance_piece = ECHIQUIER.creer_instance_piece()


def couleur_piece(position):
    ligne = 8 - int(position[1])
    colonne = ord(position[0]) - ord('a')
    piece = echiquier[ligne][colonne]

    if piece.isupper():
        return 'B'  # Pièce blanche
    elif piece.islower():
        return 'N'  # Pièce noire
    else:
        return ' '  # Case vide

def valeur_piece(position):
    ligne = 8 - int(position[1])
    colonne = ord(position[0]) - ord('a')
    return echiquier[ligne][colonne]

def format_partie_en_cours(partie_en_cours):
    formatted_moves = [f"{coup.couleur} {coup.piece} de {coup.start} à {coup.end}" for coup in partie_en_cours]
    return "\n".join(formatted_moves)

# def print_echiquierOLD():
#     for ligne in range(8):
#         for colonne in range(8):
#             position = chr(ord('a') + colonne) + str(8 - ligne)
#             valeur = echiquier[ligne][colonne]
#             piece_unicode = pieces_dict.get(valeur, valeur)
#             print(f"{position}={piece_unicode}", end='  ')
#         print()  # Passer à la ligne suivante après chaque ligne du tableau
#     print("\n")

def print_echiquier_unicode():
    for row in echiquier_unicode:
        print(" ".join(row))
    
# def print_echiquier_unicodeOLD():
#     for ligne in range(8):
#         for colonne in range(8):
#             position = chr(ord('a') + colonne) + str(8 - ligne)
#             valeur = echiquier[ligne][colonne]
#             piece_unicode = pieces_dict.get(valeur, valeur)
#             print(f"{piece_unicode}", end='  ')
#         print()  # Passer à la ligne suivante après chaque ligne du tableau
#     print("\n")
    
def print_echiquier_unicode_labels(echiquier):
    # Print column labels
    print("  A B C D E F G H")

    for ligne in range(8):
        # Print row label
        print(f"{8 - ligne}", end=' ')
        
        for colonne in range(8):
            position = chr(ord('a') + colonne) + str(8 - ligne)
            valeur = echiquier[ligne][colonne]
            piece_unicode = pieces_dict.get(valeur, valeur)
            print(f"{piece_unicode}", end='  ')
        
        print()  # Move to the next line after each row

    print("\n")

def update_echiquierOLD():
    for i in range(8):
        for j in range(8):
            piece = echiquier[i][j]
            if piece.isalpha():
                couleur = 'B' if piece.isupper() else 'N'
                nom_piece = pieces_mapping.get(piece.lower(), 'Inconnu')
                echiquier[i][j] = f"{couleur} {nom_piece}"

def validation_input(input_str):
    # Check if the separator '-' is present in the input string
    if '-' not in input_str:
        return "La séquence doit contenir le caractère '-' pour spécifier le mouvement."

    # Séparation des cases
    start, end = input_str.split('-')

    # Vérification que les deux cases sont dans la liste
    if start not in cases and end not in cases:
        return "Les deux cases ne sont pas dans la liste."
    elif start not in cases:
        return f"La case {start} n'est pas dans la liste."
    elif end not in cases:
        return f"La case {end} n'est pas dans la liste."
    else:
        couleur = couleur_piece(start)
        # couleur_end = couleur_piece(end)
        # valeur_start = valeur_piece(start)
        # piece = pieces_mapping.get(valeur_start, 'Inconnu')
        valeur_start = valeur_piece(start)
        piece_instance = creer_instance_piece(valeur_start)
        coup_joue = Coup(start, end, piece_instance, couleur)
        partie_en_cours.append(coup_joue)
        
        
        coup_joue = Coup(start, end, valeur_start, couleur)
        partie_en_cours.append(coup_joue)
        print(format_partie_en_cours(partie_en_cours))
        print([str(coup) for coup in partie_en_cours])
        # print_echiquier_unicode()
        # return f"Coup enregistré : {coup_joue}"
        return



# print("---Unicode echiquier labels ")
# print_echiquier_unicode_labels(echiquier)

# Exemple d'utilisation :
# pion_blanc = Pion(couleur='Blanc')
# tour_noire = Tour(couleur='Noir')
# cavalier_rouge = Cavalier(couleur='Rouge')
# fou_blanc = Fou(couleur='Blanc')
# reine_noire = Reine(couleur='Noir')
# roi_rouge = Roi(couleur='Rouge')

# coup = Coup(start='a1', end='b2', piece=pion_blanc)
# print(coup)

# Boucle principale
while True:
    
    # print("---echiquier_unicode ")
    print("")
    print_echiquier_unicode()
    
    input_sequence = input("Entrez une séquence de cases (par exemple, a1-a2), ou appuyez sur 'q' pour quitter : ")

    if input_sequence.lower() == 'q':
        print("Au revoir !")
        break  # Quitter la boucle si l'utilisateur entre 'q'

    validation_input(input_sequence)
    # print(result)
    # update_echiquierOLD()
    # print_echiquier_unicode()

# Afficher les coups enregistrés
print("\nCoups joués dans la partie en cours:")
for coup in partie_en_cours:
    print(coup)
