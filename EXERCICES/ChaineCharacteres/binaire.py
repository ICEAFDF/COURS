# -*- coding: utf8 -*-
"""Proportion d'une séquence dans une chaîne binaire."""

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def valide(seq):
    """Retourne vrai si la séquence est valide, faux sinon."""
    # La séquence est valide si elle est constituée uniquement de 0 et 1
    return all(c in "01" for c in seq)

def proportion(a, s):
    """Retourne la proportion de la séquence <s> dans la chaîne binaire <a>."""
    bin_s = bin(s)[2:]  # Convertir s en binaire et retirer le préfixe '0b'
    return 100 * bin(a).count(bin_s) / len(bin(a))

def saisie(ch):
    s = int(input(f"{ch} (saisir un entier) :"))
    return s

# Programme principal =========================================================
adn = saisie("chaîne binaire")
seq = saisie("séquence binaire")

print(f'Il y a {proportion(adn, seq):.2f} % de "{seq}" dans votre chaîne binaire.')

#decimal = 10
#binaire = 0b1010
#print(f"Decimal: {decimal}, Binaire: {binaire}")
