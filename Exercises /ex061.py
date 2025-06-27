# Python Exercise 061 - Arithmetic Progression V2.0
# Refaces the challenge 051, reading the first term and the reason for an AP,
# showing the first 10 terms of progression using the While structure.

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

