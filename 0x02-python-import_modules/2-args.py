#!/usr/bin/python3
def print_arg(argv):
    num = len(argv) -1
    if num == 0:
        print("{:d} arguments.".format(num))
        return
    else:
        if num == 1:
            print("{:d} argument:".format(num))
            print("{:d}: {:s}".format(num,argv))
        elif num > 1:
            print("{:d} arguments:".format(num))
        i = 1
        while i <= num:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1

if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
