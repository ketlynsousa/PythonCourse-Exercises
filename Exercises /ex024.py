# Python Exercise 024 - Checking the first letters of a text
# Write a program that reads the name of a city and says whether it starts with the name "Saint" or not.

city = str(input("Enter the city's name: ")).strip()
print(city.upper().split()[0] == 'SAINT')
