def reverse_sort(number_list):
    # Convert the input list to a tuple
    number_tuple = tuple(number_list)

    # Sort the tuple in descending order using the built-in sorted() function
    sorted_number_tuple = sorted(number_tuple, reverse=True))

    # Convert the sorted tuple back to a list
    reversed_sorted_number_list = [number for number in sorted_number_tuple]]

    return reversed_sorted_number_list