# -*- coding : utf8 -*-
"""Proportion d'une séquence dans une chaîne d'entiers."""

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def valide(seq) :
    """Retourne vrai si la séquence est valide, faux sinon."""
    ret = any(seq)
    for c in seq :
        # ret = ret and c in "atgc"
        ret = ret and c in "01"
    return ret

def proportion(a, s) :
    """Retourne la proportion de la séquence <s> dans la chaîne <a>."""
    return 100 * a.count(s) / len(a)

def saisie(ch) :
    s = input(f"{ch} :")
    while not valide(s) :
        print(f"'{ch}' ne peut contenir que les chaînons '0', '1'"
              " et ne doit pas être vide")
        s = input(f"{ch} :")
    return s

# Programme principal =========================================================
adn = saisie("chaîne")
seq = saisie("séquence")

print(f'Il y a {proportion(adn, seq):.2f} % de "{seq}" dans votre chaîne.')
# proportion(adn, seq):.2f
# : .2f => formatage qui indique comment le nombre doit être présenté pour l'affichage
# ici , flotant 2 chiffre après la
