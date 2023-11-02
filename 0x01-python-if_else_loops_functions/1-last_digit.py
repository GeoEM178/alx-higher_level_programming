#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    akherrkm = number % -10
else:
    akherrkm = number % 10
if akherrkm > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, akherrkm))
elif akherrkm < 6 and akherrkm != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, akherrkm))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))
