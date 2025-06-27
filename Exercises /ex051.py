# Python Exercise 051 - Arithmetic Progression
# Develop a program that reads the first term and the reason of an AP (arithmetic progression).
# At the end, show the first 10 terms of this progression.

term = int(input("Enter the first term of the AP: "))
reason = int(input("Enter the common difference: "))
nth_term = term + (10 - 1) * reason

print(f"\t\t\t\t\t\t\tTHE FIRST 10 TERMS")
for term in range(term, nth_term + reason , reason):
    print(f"{term} -> ", end=" ")
print("THE END.")
