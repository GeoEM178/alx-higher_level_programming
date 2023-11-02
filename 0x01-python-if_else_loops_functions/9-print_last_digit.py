#!/usr/bin/python3
def print_akherkm(number):
    if number < 0:
        akherkm = number % -(10)
        print(-(akherkm), end='')
    else:
        akherkm = number % 10
        print(akherkm, end='')
    return abs(akherkm)
