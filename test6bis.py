# Ecrire un programme qui permet de 
# saisir un nombre puis déterminer 
# s'il appartient à un intervalle donné,
#  sachant que les extrémités de 
# l'intervalle sont fixées par l'utilisateur.


n = input("Entrez une donnée numérique")
n = int(n)
i1 = input("Entrez un interval")
i1 = int(i1)
i2 = input("Entrez un interval")
i2 = int(i2)

if i1 <n < i2:
    print("n est dans l'intervale")
else:
    print("n n'est pas dans l'intervalle")