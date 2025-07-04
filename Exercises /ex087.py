# Python Exercise 087 - More about Matrix in Python
# Improve the previous challenge by showing at the end:
# A) The sum of all even values ​​entered.
# B) The sum of the values ​​in the third column.
# C) The largest value in the second row.
even_sum = sum_column3 = largest_row2 = 0
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print("Enter 9 values to make a matrix of 3x3 dimension")
print("=*" * 30)
for row in range(0, 3):
    for column in range(0, 3):
        matrix[row][column] = int(
            input(f"Enter value for row and column [{row}, {column}]: "))
print("=*" * 30)

for row in range(0, 3):
    for column in range(0, 3):
        print(f"[{matrix[row][column]:^5}]", end='')
        if matrix[row][column] % 2 == 0:
            even_sum += matrix[row][column]
    print()
print("=*" * 30)
for row in range(0, 3):
    sum_column3 += matrix[row][2]
for column in range(0, 3):
    if column == 0:
        largest_row2 = matrix[1][column]
    elif matrix[1][column] > largest_row2:
        largest_row2 = matrix[1][column]
print(f"The sum of the even numbers is {even_sum}.")
print(f"The sum of the numbers in the third columin is {sum_column3}.")
print(f"The largets value in the second row is {largest_row2}.")
