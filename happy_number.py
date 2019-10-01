def happy_number(num):
    num = str(sum([int(d) ** 2 for d in num]))
    print(num)
    while num[-1] != str(1):
        a = [int(j)**2 for j in num]
        print(sum(a))
        num = str(sum(a))

happy_number(input("Enter input: "))