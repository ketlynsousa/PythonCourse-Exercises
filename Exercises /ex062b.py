start = int(input("Enter the first term of the AP: "))
reason = int(input("Enter the common difference: "))
term = start
cont = 1
total = 0
more = 10

print(f"   \t\t\tFIRST 10 TERMS OF ARITHMETIC PROGRESSION")
print("-=" * 32)
while more != 0:
    total = total + more
    while cont <= total:
        print(f"{term} -> ", end='')
        term += reason
        cont += 1
    print("PAUSE!")
    more = int(input("Enter how many more terms you want to display or [0] to exit: "))
print(f"You displayed {total} terms initiating in the number {start} and with {reason} as common difference.")
print("THE END!")
