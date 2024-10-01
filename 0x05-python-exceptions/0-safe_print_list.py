#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_count = 0

    for i in range(x):
        try:
             print(my_list[i], end = "")
             print_count += 1

        except IndexError:
            print("\nError: Index is out of the range")
            break
    print()
    return print_count
