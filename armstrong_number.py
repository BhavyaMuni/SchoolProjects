num = int(input("Enter lower limit: "))
num1 = int(input("Enter upper limit: "))

for i in range(num, num1 + 1):
    temp = i
    tot = 0
    while temp >= 1:
        x = temp % 10
        tot += x ** 3
        temp = int(temp/10)
    if tot == i:
        print(i)
