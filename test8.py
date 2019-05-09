
# Écrire un programme qui saisie N entiers et affiche leur 
# somme et leur moyenne ?

n = input("Entrez la valeur de l'entier n:")
n = int(n)

somme = 0
for a in range(0, n+1):
    somme += a
print(somme) 

moyenne = somme/(n)
print(moyenne)


