#!/usr/bin/env python3

import random

def reverse_sort(number_list):
    """
    Sort a list of numbers in reverse order using the bubble sort algorithm.
    
    Args:
        number_list (list): A list of numbers to be sorted.
        
    Returns:
        None.
    """
    # Create an empty list to store the sorted numbers
    sorted_numbers = []
    
    # Loop through each element in the input list and swap it with the last element if it's greater than the current element
    for I in range(len(number_list) - 1, -1, -1):
        if number_list[i] > number_list[i + 1]:
            sorted_numbers.append(number_list[i])
            number_list[i] = number_list[i + 1]
            number_list[i + 1] = sorted_numbers[-1]
    
    # Return the sorted list
    return sorted_numbers

# Get the input list from the user
number_list = input("Enter a list of numbers separated by spaces: ").split()

# Call the reverse_sort function and print the sorted list
sorted_list = reverse_sort(number_list)
print("Sorted list:", sorted_list)