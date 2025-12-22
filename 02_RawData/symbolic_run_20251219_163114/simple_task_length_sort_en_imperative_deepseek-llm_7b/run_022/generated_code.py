def length_sort(string_list):
    # Sort the list by string length in ascending order
    return sorted(string_list, key=len)

# Example usage
strings = ['apple', 'orange', 'banana', 'kiwi']
sorted_strings = length_sort(strings)
print(sorted_strings)  # Output: ['apple', 'orange', 'banana', 'kiwi']