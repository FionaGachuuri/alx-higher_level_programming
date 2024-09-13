#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    sys.argv.pop(0)
    argvlen = len(sys.argv)

    if (argvlen == 0):
        print("0 arguments.")
    elif (argvlen == 1):
        print("1 argument:")
        print("{:d}: {}".format(len(sys.argv), sys.argv[0]))
    else:
        print("{:d} arguments:".format(argvlen))
        num = 1
        for arg in sys.argv:
            print("{:d}: {}".format(num, arg))
            num += 1
