
n1 = input("Entrez une donnee numerique")
n2 = input("Entrez une donnee numerique")
n1 = int(n1)
n2 = int(n2)

def calculette(operateur):
  
    if operateur == "+":
        print(n1, operateur, n2, "=", n1 + n2)
    elif operateur == "-":
        print(n1, operateur, n2, "=", n1 - n2)
    elif operateur == "/":
        if n2 == 0:
            print("operation impossible")
        else:
            print(n1, operateur, n2, "=", n1 / n2)
    else: 
        print(n1, operateur, n2, "=", n1 * n2) 
calculette("/") 