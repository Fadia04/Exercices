

operateur = input("Entrez un operateur:")
a = 0
while a < 3:
    if operateur == "+":
        print(a, operateur, a, "=", a + a)
    elif operateur == "-":
        print(a, operateur, a, "=", a - a)
    elif operateur == "/":
        if a == 0:
            print("0/0 = operation impossible")
        else:
            print(a, operateur, a, "=", a / a)
    else:
        print(a, operateur, a, "=", a * a)
    a += 1