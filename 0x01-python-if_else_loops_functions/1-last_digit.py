#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    n = number
    la = n % 10
    print("Last digit of {} is ".format(n), end="")
    if la > 5:
        print("{} and is greater than 5".format(la))
    elif la == 0:
        print("{} and is 0".format(la))
    else:
        print("{} and is less than 6 and not 0".format(la))
if number <= 0:
    n = number
    la = n % -10
    print("Last digit of {} is ".format(n), end="")
    if la == 0:
        print("{} and is 0".format(la))
    else:
        print("{} and is less than 6 and not 0".format(la))
