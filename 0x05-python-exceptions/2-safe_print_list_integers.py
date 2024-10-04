#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Attempt to print the current element as an integer
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            # Ignore non-integer values and out of range indexes
            continue
    print()  # Print a new line at the end
    return count
