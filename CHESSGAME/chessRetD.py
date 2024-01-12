cases = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4', 'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5', 'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7', 'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']

def validation_input(input_str):
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
        return "Les deux cases sont dans la liste."

# Boucle principale
while True:
    input_sequence = input("Entrez une séquence de cases (par exemple, a1-a2), ou appuyez sur 'q' pour quitter : ")

    if input_sequence.lower() == 'q':
        print("Au revoir !")
        break  # Quitter la boucle si l'utilisateur entre 'q'

    result = validation_input(input_sequence)
    print(result)
