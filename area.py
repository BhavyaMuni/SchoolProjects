def main():
    while True:
        print()
        print("To get area of Triangle enter 1. \n")
        print("To get area of Square enter 2. \n")
        print("To get area of Rectange enter 3. \n")
        print("To Exit enter 4. \n")
        print(check_inp(input("Enter your shape: ")))

def check_inp(inpu):
    if inpu == "1":
        return area_tri()
    elif inpu == "2":
        return area_sqr()
    elif inpu == "3":
        return area_rect()
    elif inpu == "4":
        exit()

def area_tri():
    b = int(input("Enter base: "))
    h = int(input("Enter height: "))
    return 0.5 * b * h

def area_sqr():
    s = int(input("Enter side: "))
    return s ** 2

def area_rect():
    l = int(input("Enter length: "))
    w = int(input("Enter width: "))
    return l * w

if __name__ == "__main__":
    main()