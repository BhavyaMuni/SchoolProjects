def machine(prods, arr, coins):
    while True:
        print("Welcome to the vending machine.")
        print("What would you like buy? \n")

        for i in prods:
            print(prods.index(i)+1," ", i, items[prods.index(i)+1])

        item = int(input("\nEnter the item you want to buy: \n"))

        price = arr[item]
        current = 0
        print()
        print("0 for 5/-\n1 for 10/-\n2 for 20/-")

        while current != price:
            try:
                current += coins[int(input("Enter value of coins: \n"))]
            except IndexError:
                print("invalid coin value")
                break
            if current < price:
                print("You have entered {} ruppees.".format(current))
                print("You need to enter {} more ruppees.\n".format(price-current))
            if current > price:
                print("The change is {} ruppees".format(current-price))
                print("Thank you for purchasing \n")
                break
            elif current == price:
                print("Thank you for purchasing \n")

prods = ["Coke", "Pringles", "Sprite", "Maggie"]
items = {1: 50, 2:40, 3:200, 4: 20}
coins = [5, 10, 20]

if __name__ == "__main__":
    machine(prods,items, coins)
