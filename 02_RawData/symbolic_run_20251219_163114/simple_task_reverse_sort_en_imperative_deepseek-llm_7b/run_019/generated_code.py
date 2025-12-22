def reverse_sort(number_list):
    return sorted(number_list, reverse=True)

# Test the function with some sample data
numbers = [4, 2, 9, 6]
sorted_numbers = reverse_sort(numbers)
print(sorted_numbers)  # Output: [9, 6, 4, 2]