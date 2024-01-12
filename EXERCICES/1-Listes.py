fruits = ["pomme", "banane", "orange", "fraise", "kiwi", "raisin", "Ananas", "mangue", "poire", "cerise"]

# 1- afficher tous les fruits avec un a
# 2- afficher tous les fruits avec un a et un n
# 3- afficher tous les fruits avec un a et un N


# 1- Afficher tous les fruits avec un 'a'
fruits_avec_a = [fruit for fruit in fruits if 'a' in fruit]
print("Fruits avec un 'a' :", fruits_avec_a)

# 2- Afficher tous les fruits avec un 'a' et un 'n'
fruits_avec_a_et_n = [fruit for fruit in fruits if 'a' in fruit and 'n' in fruit]
print("Fruits avec un 'a' et un 'n' :", fruits_avec_a_et_n)

# 3- Afficher tous les fruits avec un 'a' et un 'N'
fruits_avec_a_et_N = [fruit for fruit in fruits if 'a' in fruit and 'N' in fruit]
print("Fruits avec un 'a' et un 'N' :", fruits_avec_a_et_N)
