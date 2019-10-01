lent = int(input("Enter length of array: "))
num = [] 
for i in range(lent):
    num.append(int(input("Enter number {}: ".format(i+1))))
print(sum(num))

