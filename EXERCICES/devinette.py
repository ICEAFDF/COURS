import random

# Génération d'un nombre secret entre 1 et 100
nombre_secret = random.randint(1, 100)

# Initialisation de la variable de devinette et du nombre de tentatives
devinette = 0
nombre_tentatives = 0

# Boucle while tant que la devinette n'est pas correcte
while devinette != nombre_secret:
    # Demande à l'utilisateur de deviner le nombre
    devinette = int(input("Devinez le nombre secret entre 1 et 100 : "))
    
    # Incrémentation du nombre de tentatives
    nombre_tentatives += 1

    # Vérification de la devinette
    if devinette < nombre_secret:
        print(f"Le nombre secret est plus grand. Essayez à nouveau. {nombre_tentatives} tentatives")
    elif devinette > nombre_secret:
        print(f"Le nombre secret est plus petit. Essayez à nouveau. {nombre_tentatives} tentatives")
    else:
        print(f"Félicitations ! Vous avez deviné le nombre secret {nombre_secret} en {nombre_tentatives} tentatives.")
