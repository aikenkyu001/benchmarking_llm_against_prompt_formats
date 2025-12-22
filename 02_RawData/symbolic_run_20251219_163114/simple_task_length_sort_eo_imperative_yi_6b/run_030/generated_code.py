def length_sort(string_list):
    # Use the built-in sort method on the list, which uses Timsort (a hybrid sorting algorithm derived from merge sort and insertion sort)
    return sorted(string_list, key=len)

# Test the function with a sample list of strings
strings = ["apple", "banana", "cherry", "date"]
sorted_by_length = length_sort(strings)
print(sorted_by_length)  # Output: ['date', 'apple', 'banana', 'cherry']