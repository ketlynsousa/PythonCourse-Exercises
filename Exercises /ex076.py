# Python Exercise 076 - Price List with Tuple
# Create a program that has a single tuple with product names and their respective prices, in sequence.
# At the end, show a price list, organizing the data in tabular form.
shopping_list = ('Pencil', 1.75, 'Eraser', 2, 'Notebook', 15.90, 'Pen case', 25, 'Protractor ruler', 4.20, 'Drawing compass', 9.99,
                 'Backpack', 120.32, 'Pens', 22.30, 'Books', 34.90)

print('-' * 60)
print(f"{'PRICE LIST':^60}")
print('-' * 60)

for item in range(0, len(shopping_list)):
    if item % 2 == 0:
        print(f"{shopping_list[item]:.<35}", end='')
    else:
        print(f"${shopping_list[item]:>7.2f}")
