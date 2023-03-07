#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        num = number % 10
    else:
        n = -number
        num = n % 10
    print(num, end="")
    return num
