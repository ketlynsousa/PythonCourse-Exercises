# Python Exercise 029 - Electronic radar
# Write a program that reads the speed of a car. If it exceeds 80 km/h, display a message saying that it has been fined.
# The fine will cost R$7.00 for each km over the limit.

colors = {'clean': '\033[m',
         'green': '\033[32m',
         'yellow':'\033[33m',
         'red': '\033[31m'}

car_speed = float(input("Enter the speed in Km/h: "))
speed_fine = (car_speed - 80) * 7
if car_speed > 80:
    print(f"{colors['yellow']}STOP! You exceeded the speed limit.{colors['clean']}")
    print(f"{colors['red']}You have been fined. The amount of the fine is ${speed_fine:.2f}.{colors['clean']}")
else:
    print(f"{colors['green']}You are within the limit of the road. Have a good trip.{colors['clean']}")
