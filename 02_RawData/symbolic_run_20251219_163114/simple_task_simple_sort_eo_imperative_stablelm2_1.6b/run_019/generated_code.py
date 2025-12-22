def simple_sort(number_list):
    # Sort the input list using the sorted() function
    sorted_list = sorted(number_list)
    
    return sorted_list

# Example usage:
numbers = [5, 2, 8, 1, 9]
sorted_numbers = simple_sort(numbers)
print(sorted_numbers)  # Output: [1, 2, 5, 8, 9]