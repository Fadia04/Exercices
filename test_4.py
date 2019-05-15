

donnee1 = input("Entrez une donnee numerique:")
donnee2 = input("Entrez une donnee numerique:")
operateur = input("Entrez un operateur:")
donnee1 = int(donnee1)
donnee2 = int(donnee2)
if operateur == "+":
    print(donnee1, operateur, donnee2, "=", donnee1 + donnee2)
elif operateur == "-":
    print(donnee1, operateur, donnee2, "=", donnee1 - donnee2)
elif operateur == "/":
    if donnee2 == 0:
        print("0/0 = operation impossible")
    else:
        print(donnee1, operateur, donnee2, "=", donnee1 / donnee2)
else:
    print(donnee1, operateur, donnee2, "=", donnee1 * donnee2)