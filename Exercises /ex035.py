# Python Exercise 035 - Analyzing Triangle v1.0
# Develop a program that reads the length of three lines and tells the user whether they can form a triangle or not.
print('=*' * 15)
print("\033[34mTRIANGLE ANALYZER\033[m".center(40))
print('=*' * 15)
length1 = float(input("Length of the first straight line: "))
length2 = float(input("Length of the second straight line: "))
length3 = float(input("Length of the third straight line: "))

if (length1 + length2 > length3) and (length1 + length3 > length2) and (length2 + length3 > length1):
    print(f"With the lengths \033[35m{length1, length2, length3}. \033[32mYOU CAN FORM A TRIANGLE.\033[m")
else:
    print(f"With the lengths \033[35m{length1, length3, length3}. \033[31mYOU CANNOT FORM A TRIANGLE.\033[m")
