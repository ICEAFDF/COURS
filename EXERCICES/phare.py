# -*- coding : utf8 -*-
"""Gardien de phare."""

def hauteurParcourue(nb, h, n_jours=7):
    n_allerRetourpar_jour  = 3
    aller = 1
    retour = 1
    aller_retour = aller + retour
    
    distance_parcourue = nb * h * aller_retour * n_allerRetourpar_jour  * n_jours / 100.0
    result = "Pour {:d} marches de {:d} cm, il parcourt {:.2f} m par semaine !".format(nb, h, distance_parcourue)
    return result

nbMarches = int(input("Combien de marches ? "))
hauteurMarche = int(input("Hauteur d'une marche (cm) ? "))

resultat = hauteurParcourue(nbMarches, hauteurMarche)
print(resultat)


# Un gardien de phare va à la cuisine 3 fois par jour. Or la cuisine sont au rez-de-chaussée…

# Écrire une procédure hauteurParcourue qui reçoit deux paramètres, 
# le nombre de marches du phare et la hauteur de chaque marche (en cm), et qui affiche :

#  Sélectionnez
# Pour x marches de y cm, il parcourt z.zz m par semaine.
# On n'oubliera pas :

# qu'une semaine comporte 7 jours ;
# qu'une fois en bas, le gardien doit remonter ;