#!/usr/bin/python3
"""Print numbers from 1 o 100 seperated by a space
    For x3 Fizz
    for x5 Buzz
    for x3&5 Fizzuzzz
    else the number
    """


def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz ")
        elif i % 3 == 0:
            print("Fizz ")
        elif i % 5 == 0:
            print("Buzz ")
        else:
            print(i)
