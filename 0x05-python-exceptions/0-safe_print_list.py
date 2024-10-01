#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            if i < len(my_list):
                print(my_list[i], end = "")
                count += 1
            else:
                break
        print()
        return count
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
