

donnée1 = input("Entrez une donnée numérique:")
donnée2 = input("Entrez une donnée numérique:")
operateur = input("Entrez un opérateur:")
donnée1 = int(donnée1)
donnée2 = int(donnée2)
if operateur == "+":
    print(donnée1, operateur, donnée2, "=", donnée1 + donnée2)
elif operateur == "-":
    print(donnée1, operateur, donnée2, "=", donnée1 - donnée2)
elif operateur == "/":
    print(donnée1, operateur, donnée2, "=", donnée1 / donnée2)
else:
    print(donnée1, operateur, donnée2, "=", donnée1 * donnée2)
  