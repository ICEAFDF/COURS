# -*- coding : utf8 -*-
"""kCHESS2024_classes.py"""
"""Jeu d'Echecs v0.5"""

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
            ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
            ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
        ]
        
        self.echiquier_unicode_noirs = [
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
            'P': Pion, 'p': Pion,
            'T': Tour, 't': Tour,
            'C': Cavalier, 'c': Cavalier,
            'F': Fou, 'f': Fou,
            'D': Reine, 'd': Reine,
            'R': Roi, 'r': Roi,
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

        # Nouvelle variable pour stocker l'échiquier Unicode actuel
        self.echiquier_unicode_actuel = self.echiquier_unicode

    def changer_orientation(self):
        # Inverser l'échiquier Unicode actuel
        self.echiquier = [ligne[::-1] for ligne in self.echiquier]
        self.echiquier_unicode = [ligne[::-1] for ligne in self.echiquier_unicode]

    def print_echiquier(self):
        for row in self.echiquier:
            print(' '.join(row))
        print()

    # def print_echiquier_unicode(self):
    #     for ligne in range(8):
    #         for colonne in range(8):
    #             piece_unicode = self.echiquier_unicode[ligne][colonne]
    #             print(f"{piece_unicode}", end='  ')
    #         print()
    
    def print_echiquier_unicode(self, couleur='B'):
        if couleur == 'N':
            echiquier_unicode = self.echiquier_unicode_noirs
        else:
            echiquier_unicode = self.echiquier_unicode

        for ligne in range(8):
            for colonne in range(8):
                piece_unicode = echiquier_unicode[ligne][colonne]
                print(f"{piece_unicode}", end='  ')
            print()
class ECHIQUIER:
    def __init__(self):
        self.partie_en_cours = []
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

        self.echiquier_unicode_noirs = [
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
            'P': Pion, 'p': Pion,
            'T': Tour, 't': Tour,
            'C': Cavalier, 'c': Cavalier,
            'F': Fou, 'f': Fou,
            'D': Reine, 'd': Reine,
            'R': Roi, 'r': Roi,
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

        # Nouvelle variable pour stocker l'échiquier Unicode actuel
        self.echiquier_unicode_actuel = self.echiquier_unicode

        # Liste pour stocker les coups joués
        self.coups_joues = set()

    def changer_orientation(self):
        # Inverser l'échiquier Unicode actuel
        self.echiquier = [ligne[::-1] for ligne in self.echiquier]
        self.echiquier_unicode = [ligne[::-1] for ligne in self.echiquier_unicode]

    def print_echiquier(self):
        for row in self.echiquier:
            print(' '.join(row))
        print()

    def print_echiquier_unicode(self, couleur='B'):
        if couleur == 'N':
            echiquier_unicode = self.echiquier_unicode_noirs
        else:
            echiquier_unicode = self.echiquier_unicode_actuel  # Utilisez l'échiquier Unicode actuel

        for ligne in range(8):
            for colonne in range(8):
                piece_unicode = echiquier_unicode[ligne][colonne]
                print(f"{piece_unicode}", end='  ')
            print()


    def print_echiquier_unicode_noirs(self):
        for ligne in range(8):
            for colonne in range(8):
                piece = self.echiquier[ligne][colonne]
                if (ligne, colonne) in self.cases:
                    if piece != ' ':
                        if piece.couleur == 'B':
                            print(f' {piece.symbole_blanc()} ', end='')
                        elif piece.couleur == 'N':
                            print(f' {piece.symbole_noir()} ', end='')
                    else:
                        if (ligne, colonne) in self.coups_joues:
                            print(' . ', end='')  # Affiche un point pour indiquer que la case a été jouée
                        else:
                            print('   ', end='')
                else:
                    print('   ', end='')
            print('')



    def make_move(self, start, end, inverse=False):
        ligne_start = 8 - int(start[1])
        colonne_start = ord(start[0]) - ord('a')

        ligne_end = 8 - int(end[1])
        colonne_end = ord(end[0]) - ord('a')

        # Inverser l'échiquier si nécessaire
        if inverse:
            ligne_start, colonne_start = 7 - ligne_start, 7 - colonne_start
            ligne_end, colonne_end = 7 - ligne_end, 7 - colonne_end

        # Mettre à jour l'échiquier
        piece = self.echiquier[ligne_start][colonne_start]
        # Déplacez la pièce de la case de départ à la case d'arrivée
        self.echiquier[ligne_start][colonne_start] = ' '
        self.echiquier[ligne_end][colonne_end] = piece

        # Mettre à jour l'échiquier Unicode également
        piece_unicode = self.echiquier_unicode[ligne_start][colonne_start]
        self.echiquier_unicode[ligne_start][colonne_start] = ' '
        self.echiquier_unicode[ligne_end][colonne_end] = piece_unicode

        # Si inverse est True, inversez les rôles des couleurs (noir devient blanc et vice versa)
        if inverse:
            self.partie_en_cours[-1].couleur = 'B' if self.partie_en_cours[-1].couleur == 'N' else 'N'

        # Ajoutez la case de départ et d'arrivée à la liste des coups joués
        self.coups_joues.add(start)
        self.coups_joues.add(end)

        # Mettez à jour l'échiquier Unicode actuel
        if inverse:
            self.echiquier_unicode_actuel = [ligne[::-1] for ligne in self.echiquier_unicode]
        else:
            self.echiquier_unicode_actuel = self.echiquier_unicode



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

    def check_bouger_piece(self, start, end):
        # Converti les coordonnées de la case de départ et de la case d'arrivée
        ligne_start, colonne_start = 8 - int(start[1]), ord(start[0]) - ord('a')
        ligne_end, colonne_end = 8 - int(end[1]), ord(end[0]) - ord('a')

        # Implémente la logique de déplacement du Pion
        if self.couleur == 'B':  # Pion blanc
            # Si c'est le premier mouvement, le Pion peut avancer d'une ou deux cases
            if ligne_start == 6 and ligne_start - ligne_end in (1, 2):
                return True
            # Sinon, le Pion peut avancer d'une case
            elif ligne_start - ligne_end == 1:
                return True
        elif self.couleur == 'N':  # Pion noir
            # Si c'est le premier mouvement, le Pion peut avancer d'une ou deux cases
            if ligne_start == 1 and ligne_end - ligne_start in (1, 2):
                return True
            # Sinon, le Pion peut avancer d'une case
            elif ligne_end - ligne_start == 1:
                return True

        # Si aucune des conditions ci-dessus n'est remplie, le déplacement n'est pas autorisé
        return False

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
    def __init__(self, start, end, piece, couleur, echiquier):
        self.start = start
        self.end = end
        self.couleur = couleur
        self.echiquier = echiquier
        self.piece = self.creer_instance_piece(piece)

    def creer_instance_piece(self, piece_str):
        # Utilisez votre mapping pour créer une instance de la classe de pièce appropriée
        piece_key = piece_str.upper()
        if piece_key in self.echiquier.pieces_mapping:
            classe_piece = self.echiquier.pieces_mapping[piece_key]
            return classe_piece(couleur=self.couleur)
        else:
            print(f"Type de pièce inconnu : {piece_str}")
            raise ValueError(f"Type de pièce inconnu : {piece_str}")

    def __str__(self):
        return f"{self.piece.__class__.__name__} de {self.start} à {self.end}"