# Ecrire un programme permettant de lire un nombre
#  entier N puis calcule son factoriel.
# Utilisez tant que,
# Utilisez pour.

n = input("Entrez un nombre entier n:")
n = int(n)       
a = 1 
f = 1

while a <= n:
    f = f * a 
    a += 1  
if n == 0:
    print(1) 
elif n < 0:
    print("n n'est pas un entier")
else:
    print(f)