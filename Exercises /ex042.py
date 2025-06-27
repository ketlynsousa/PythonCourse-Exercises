# Python Exercise 042 - Analyzing Triangles v2.0
# Redo CHALLENGE 035 of triangles, adding the feature to show what type of triangle will be formed:
# - EQUILATERAL: all sides equal
# - ISOSCELES: two sides equal, one different
# - SCALENE: all sides different
print('=*' * 15)
print("\033[34mTRIANGLE ANALYZER\033[m".center(40))
print('=*' * 15)
length1 = float(input("Length of the first straight line: "))
length2 = float(input("Length of the second straight line: "))
length3 = float(input("Length of the third straight line: "))

if (length1 + length2 > length3) and (length1 + length3 > length2) and (length2 + length3 > length1):
    print(f"With the lengths \033[35m{length1, length2, length3}. \033[32mYOU CAN FORM A TRIANGLE.\033[m")
    if length1 == length2 == length3:
        print(f"It forms an EQUILATERAL triangle, since all sides are equal!")
    elif length1 != length2 != length3 != length1:
        print(f"It forms a \033[1m SCALENE triangle\033[m, because all sides are different!")
    else:
        print(f"It forms an ISOSCELES triangle, as it has two equal sides and one different side!")
else:
    print(f"With the lengths \033[35m{length1, length3, length3}. \033[31mYOU CANNOT FORM A TRIANGLE.\033[m")
