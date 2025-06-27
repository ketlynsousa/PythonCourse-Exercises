# Python Exercise 043 - Body Mass Index
# Develop a logic that reads a person's weight in Kg and height in meters, for instance, 1.70. Calculates their Body Mass Index (BMI)
# and displays their status, according to the table below:
# - BMI below 18.5: Underweight
# - Between 18.5 and 25: Ideal Weight
# - 25 to 30: Overweight
# - 30 to 40: Obesity
# - Over 40: Morbid Obesity

print("Let's calculate your body mass index (BMI)!")
weight = float(input("Enter your weight in Kg: "))
heigh = float(input("Enter your heigh in meters: "))

BMI = weight / (heigh * heigh)

if BMI < 18.5:
    print(f"Your BMI is {BMI:.1f}. \033[31mYou are underweight!\033[m")
elif 18.5 <= BMI < 25:
    print(f"Your BMI is {BMI:.1f}. \033[32mYou are at a ideal weight!\033[m")
elif 25 <= BMI < 30:
    print(f"Your BMI is {BMI:.1f}. \033[33mYou are overweight!\033[m")
elif 30 <= BMI <= 40:
    print(f"Your BMI is {BMI:.1f}. \033[31mYou are at the level of obesity!\033[m")
else:
    print(f"Your BMI is {BMI:.1f}. \033[31mYou are at the level of morbid obesity!\033[m")
