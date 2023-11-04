#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    neww = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            neww.append(True)
        else:
            neww.append(False)
    return (neww)
