from math import factorial

lent = int(input("Enter length: "))

def comb(n, r):
    return factorial(n)/(factorial(r) * factorial(n-r))

for i in range(0, lent):
    for j in range(0, i):
        print(str(comb(i, j))[0:-2], end=" ")
    print("1", end = "")
    print()