# Ecrire un programme permettant de lire un nombre
#  entier N puis calcule son factoriel.
# Utilisez tant que,
# Utilisez pour.

n = input("Entrez un nombre entier n:")
n = int(n)
f = 1
if n<0:
    print("n n'est pas un entier positif")
elif n == 0:
    print("f = 1")
else:
    for a in range(1, n+1):
        f = f * a
    print(f)


