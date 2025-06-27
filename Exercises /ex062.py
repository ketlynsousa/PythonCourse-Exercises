# Python Exercise 062 - Super Arithmetic Progression V3.0
# Improve Challenge 061 by asking the user if he wants to display some more terms.
#Program will end when he says he wants to display 0 the terms.
start = int(input("Enter the first term of the AP: "))
reason = int(input("Enter the common difference: "))
term = start
cont = 1

print(f"   \t\t\tFIRST 10 TERMS OF ARITHMETIC PROGRESSION")
print("-=" * 32)
while cont <= 10:
    print(f"{term} -> ", end='')
    term += reason
    cont += 1
print("THE END!")

option = 1
while option != 0:
    option = int(input("Enter [1] to display more or [0] to exit: "))
    if option == 1:
        start = int(input("Enter the first term of the AP: "))
        reason = int(input("Enter the common difference: "))
        term = start
        cont = 1

        print(f"   \t\t\tFIRST 10 TERMS OF ARITHMETIC PROGRESSION")
        print("-=" * 32)
        while cont <= 10:
            print(f"{term} -> ", end='')
            term += reason
            cont += 1
        print("FIM!")
    elif option == 0:
        print("Program closed.")
    else:
        print("Invalid option. Try again.")
