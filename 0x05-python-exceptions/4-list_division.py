#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            # Attempt dividing elements of both lists
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            # find division by zero
            print("division by 0")
            result = 0
        except (TypeError, ValueError):
            # find wrong type
            print("wrong type")
            result = 0
        except IndexError:
            # find out of range error
            print("out of range")
            result = 0
        finally:
            # Append the result to the new list regardless of any exceptions
            new_list.append(result)
    return new_list
