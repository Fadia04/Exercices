
# Ecrire un programme qui demande deux 
# nombres à l’utilisateur etl’informe
#  ensuite si leur produit est négatif 
# ou positif. Attention toutefois :on 
# ne doit pas calculer le produit des
# deux nombres.

n1 = input("Entrez une donnée numérique")
n2 = input("Entrez une donnée numérique")
n1 = int(n1)
n2 = int(n2)
p = n1 * n2
if p < 0:
    print("p est négatif")
else:
    print("p est positif")