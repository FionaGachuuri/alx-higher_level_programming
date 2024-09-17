def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
# Start by assuming the first element is the largest
    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num
# Update max_val if a larger number is found
    return max_value
