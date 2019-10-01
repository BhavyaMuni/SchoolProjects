# num = int(input("Enter num: "))

# for j in range(2, 10):
#     if (int(num) % j == 0):
#         print("Not Prime number.")
#         break

# else:
#     print("Prime")

num = int(input("Enter lowest val: "))
num1 = int(input("Enter highest val: "))

for i in range(num, num1 + 1):
    for j in range(2, 10):
        if (i % j == 0):
            break
    else:
        print(i)