# Python Exercise 086 - Matrix in Python
# Create a program that declares a 3x3 matrix and fills it with values ​​read from the keyboard.
# At the end, display the matrix on the screen, with the correct formatting.

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
    print()
