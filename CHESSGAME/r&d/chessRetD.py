class Fou:
    def __init__(self, couleur):
        self.couleur = couleur

class Reine:
    def __init__(self, couleur):
        self.couleur = couleur

class PromoPion:
    def __init__(self, couleur):
        self.couleur = couleur

class Tour:
    def __init__(self, couleur):
        self.couleur = couleur

class Coup:
    def __init__(self, start, end, piece, couleur):
        self.start = start
        self.end = end
        self.piece = piece
        self.couleur = couleur

    def __str__(self):
        return f"{self.couleur} {self.piece} de {self.start} à {self.end}"

partie_en_cours = []

# Maj : blanc  Min : noir
echiquier = [
    ['t', 'c', 'f', 'd', 'r', 'f', 'c', 't'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['T', 'C', 'F', 'D', 'R', 'F', 'C', 'T']
]

pieces_mapping = {
    'P': 'Pion',
    'p': 'Pion',
    'T': 'Tour',
    't': 'Tour',
    'C': 'Cavalier',
    'c': 'Cavalier',
    'F': 'Fou',
    'f': 'Fou',
    'D': 'Dame',
    'd': 'Dame',
    'R': 'Roi',
    'r': 'Roi',
}

cases = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'a3', 'b3', 'c3',
         'd3', 'e3', 'f3', 'g3', 'h3', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4', 'a5', 'b5', 'c5', 'd5', 'e5', 'f5',
         'g5', 'h5', 'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7', 'a8',
         'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']

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

def print_echiquier():
    for row in echiquier:
        print(" ".join(row))
    print("\n")

def validation_input(input_str):
    # Check if the separator '-' is present in the input string
    if '-' not in input_str:
        return "La séquence doit contenir le caractère '-' pour spécifier le mouvement."

    # Séparation des cases
    start, end
