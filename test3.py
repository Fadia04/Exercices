

operateur = input("Entrez un operateur:")
a = 1
while a < 3:
    if operateur == "+":
        print(a, operateur, a, "=", a + a)
    elif operateur == "-":
        print(a, operateur, a, "=", a - a)
    elif operateur == "/":
        print(a, operateur, a, "=", a / a)
    else:
        print(a, operateur, a, "=", a * a)
    a += 1