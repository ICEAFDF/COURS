# Exercice : Trouvez le résultat de chaque fonction



















# Testez les fonctions avec des valeurs de votre choix et essayez de deviner les résultats.

# Exemple :
# resultat_fonction_1 = moyenne_liste([85, 90, 92, 88, 95])
# print("Résultat de la fonction 1a :", resultat_fonction_1)


# --------------------------------------------------------------------

# Exercice : Trouvez et corrigez les erreurs dans chaque fonction

# Fonction 1
# carre_nombre
def function_1(x):
    return x ** 2

# Fonction 2
# addition_liste
def function_2(liste):
    total = 0
    for element in liste:
        total += element
    return total

# Fonction 3
# produit_liste
def function_3(liste):
    resultat = 1
    for element in liste:
        resultat *= element
    return resultat

# Fonction 4
# est_majeur
def function_4(age):
    return age >= 18

# Fonction 5
# longueur_chaine
def function_5(texte):
    return len(texte)

# Fonction 6
# inverser_liste
def function_6(ma_liste):
    return ma_liste[::-1]

# Fonction 7
# puissance_deux
def function_7(n):
    return 2 ** n

# Fonction 8
# moyenne_deux_nombres
def function_8(a, b):
    return (a + b) / 2

# Fonction 9
# tri_croissant
def function_9(liste):
    return sorted(liste)

# Fonction 10
# somme_pairs_jusqu_a_n
def function_10(n):
    return sum(x for x in range(1, n+1) if x % 2 == 0)

# Fonction 11
# moyenne_liste
def function_11(notes):
    return sum(notes) / len(notes)

# Fonction 12
# puissance_reciproque
def function_12(a, b):
    return a ** (1 / b)

# Fonction 13
# est_palindrome
def function_13(mot):
    mot_inverse = mot[::-1]
    return mot == mot_inverse

# Fonction 14
# somme_pairs
def function_14(liste):
    return sum(x for x in liste if x % 2 == 0)

# Fonction 15
# enlever_doublons
def function_15(liste):
    return list(set(liste))

# Fonction 16
# calcul_factoriel
def function_16(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * function_16(n - 1)

# Fonction 17
# trier_liste
def function_17(liste):
    return sorted(liste)

# Fonction 18
# somme_carrés_pairs
def function_18(n):
    return sum(x**2 for x in range(1, n+1) if x % 2 == 0)

# Fonction 19
# calculer_moyenne_ponderee
def function_19(notes, poids):
    return sum(note * poids for note, poids in zip(notes, poids)) / sum(poids)

# Fonction 20
# est_anagramme
def function_20(mot1, mot2):
    return sorted(mot1) == sorted(mot2)

# ------------------------------------------------------Questions :
resultat_fonction_1 = function_1(5)
resultat_fonction_2 = function_2([1, 2, 3, 4, 5])
resultat_fonction_3 = function_3([1, 2, 3, 4, 5])
resultat_fonction_4 = function_4(20)
resultat_fonction_5 = function_5("Python")
resultat_fonction_6 = function_6([1, 2, 3, 4, 5])
resultat_fonction_7 = function_7(3)
resultat_fonction_8 = function_8(5, 7)
resultat_fonction_9 = function_9([3, 1, 4, 1, 5, 9, 2, 6, 5])
resultat_fonction_10 = function_10(6)
resultat_fonction_11 = function_11([85, 90, 92, 88, 95])
resultat_fonction_12 = function_12(8, 3)
resultat_fonction_13 = function_13("radar")
resultat_fonction_14 = function_14([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
resultat_fonction_15 = function_15([1, 2, 2, 3, 4, 4, 5])
resultat_fonction_16 = function_16(5)
resultat_fonction_17 = function_17([3, 1, 4, 1, 5, 9, 2, 6, 5])
resultat_fonction_18 = function_18(4)
notes = [85, 90, 92, 88, 95]
poids = [0.2, 0.3, 0.2, 0.1, 0.2]
resultat_fonction_19 = function_19(notes, poids)
resultat_fonction_20 = function_20("arbre", "barre")

print("Résultat de la fonction 1 :", resultat_fonction_1)
print("Résultat de la fonction 2 :", resultat_fonction_2)
print("Résultat de la fonction 3 :", resultat_fonction_3)
print("Résultat de la fonction 4 :", resultat_fonction_4)
print("Résultat de la fonction 5 :", resultat_fonction_5)
print("Résultat de la fonction 6 :", resultat_fonction_6)
print("Résultat de la fonction 7 :", resultat_fonction_7)
print("Résultat de la fonction 8 :", resultat_fonction_8)
print("Résultat de la fonction 9 :", resultat_fonction_9)
print("Résultat de la fonction 10 :", resultat_fonction_10)
print("Résultat de la fonction 11 :", resultat_fonction_11)
print("Résultat de la fonction 12 :", resultat_fonction_12)
print("Résultat de la fonction 13 :", resultat_fonction_13)
print("Résultat de la fonction 14 :", resultat_fonction_14)
print("Résultat de la fonction 15 :", resultat_fonction_15)
print("Résultat de la fonction 16 :", resultat_fonction_16)
print("Résultat de la fonction 17 :", resultat_fonction_17)
print("Résultat de la fonction 18 :", resultat_fonction_18)
print("Résultat de la fonction 19 :", resultat_fonction_19)
print("Résultat de la fonction 20 :", resultat_fonction_20)