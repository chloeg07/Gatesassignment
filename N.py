import Gates
Menu = print("Choose one of the following gates , \n1 = NOT \n2 = AND \n3 = OR \n4 = XOR \n5 = NAND \n6 = NOR \n7 = XNOR")
MenuChoice = int(input("Input -->  "))

if MenuChoice == 1:
    print("You have chosen NOT gate")
    print("Do you want to see the truth table?")
    choice = input("y or n -->  ")
    if choice == "y":
        print("A A(NOT)\n0 1\n1 0")
    input1 = int(input("Enter value for the NOT gate  "))
    print(Gates.NOT_Gate(input1))