def reverse_sort(number_list):
    # Convert the input list to a set for faster membership testing
    number_set = set(number_list)

    # Reverse the order of elements in the set
    reversed_number_set = number_set[::-1]

    # Convert the reversed set back to a list
    reversed_number_list = list(reversed_number_set))

    return reversed_number_list

# Test the function with an example input list
number_list = [5, 3, 9, 2, 7], 4
reversed_sorted_list = reverse_sort(number_list)
print("Reversed sorted list:", reversed_sorted_list))