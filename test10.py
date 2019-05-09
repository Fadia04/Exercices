

n = input("Entrez un nombre entier n:")
n = int(n)       

f = 1
while n < 5:
    for a in range(1, n + 1):
        f = f * a 
    print(f)
    n +=1