#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = number % -10
elif number > 0:
    last_digit = number % 10
if last_digit > 5:
    print("The last digit of {} is {} and is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print("The last digit of {} is {} and is 0".format(number, last_digit))
elif last_digit < 6 & last_digit != 0:
    print("The last digit of {} is {} and is less than 6 and not 0".format(number, last_digit))