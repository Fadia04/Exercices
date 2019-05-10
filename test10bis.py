
# Ecrire un programme permettant de lire un nombre
#  entier N puis calcule son factoriel.
# Utilisez tant que,
# Utilisez pour.

n = input("Entrez un nombre entier n:")
n = int(n)       
f = 1

while n < 5:
    for a in range(1, n+1):
        f = f * a 
    if n<=0:   
        print("x")
    else:
        print(f)
        n += 1
   