import sys

def main():
    menu()

def Ground_Shipping():
    weight = int(input("Please enter your weight: "))
    if weight <= 2:
        cost = (weight * 1.50 + 20.00)
    elif weight > 2 or weight == 6:
        cost = (weight * 3.00 + 20.00)
        print(cost)
    elif weight > 6 or weight == 10:
        cost = (weight * 4.00 + 20.00)
        print(cost)
    elif weight > 10:
        cost = (weight * 4.75 + 20.00)
        print(cost)
    else:
        print("Please enter a vaild number: ")
        return weight()

def Drone_Shipping():
    weight = int(input("Please enter your weight: "))
    if weight <= 2:
        cost = (weight * 4.50 + 0.00)
        print(cost)
    elif weight > 2 or weight == 6:
        cost = (weight * 9.00 + 0.00)
        print(cost)
    elif weight > 6 or weight == 10:
        cost = (weight * 12.00 + 0.00)
        print(cost)
    elif weight > 10:
        cost = (weight * 14.25 + 0.00)
        print(cost)
    else:
        print("Please enter a vaild number: ")
        return weight()

def menu():
    print("Welcome to Sal's Shipping Menu")
    print("[1] Ground Shipping")
    print("[2] Drone Shipping")
    print("[3] Exit Menu")
    option = int(input("Which option do you select: "))
    if option == 1:
        Ground_Shipping()
    elif option == 2:
        Drone_Shipping()
    elif option == 3:
        print("Thanks for using ")
        sys.exit()
    else:
        print("Please select the right option next time")
        menu()

main()