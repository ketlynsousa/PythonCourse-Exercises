# Python Exercise 083 - Validating mathematical expressions
# Create a program where the user enters any expression that uses parentheses.
# Your application should analyze whether the passed expression has the open and closed parentheses in the correct order.

expression = str(input("Enter an expression: "))
entry = []
for symbol in expression:
    if symbol == '(':
        entry.append('(')
    elif symbol == ')':
        if len(entry) > 0:
            entry.pop()
        else:
            entry.append(')')
            break
if len(entry) == 0:
    print("Your expression is correct.")
else:
    print("Your expression is not correct.")
