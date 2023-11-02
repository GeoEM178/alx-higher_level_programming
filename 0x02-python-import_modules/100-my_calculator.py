#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def calcTheArgu(argv):
    n = len(argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <mathOperator> <b>")
        exit(1)
    a = int(argv[1])
    mathOp = argv[2]
    b = int(argv[3])
    if mathOp == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, mathOp, b, add(a, b)))
    elif mathOp == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, mathOp, b, sub(a, b)))
    elif mathOp == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, mathOp, b, mul(a, b)))
    elif mathOp == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, mathOp, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    import sys
    calcTheArgu(sys.argv)
