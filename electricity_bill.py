def calculate_bill(unit):
    tot = 0
    charge = [300, 50, 100]
    price = [0, 0.1, 0.3]

    for i in range(0, len(charge)):

        if (unit - charge[i]) <= 0:
            tot += unit * price[i]
            unit = 0
            break
        else:
            tot += (charge[i] * price[i])
            unit -= charge[i]

        # print(tot)
    tot += unit * 2
    return tot

units = int(input("Enter units consumed: "))
print("Your reciept is: ${}".format(calculate_bill(units)))
