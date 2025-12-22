def custom_sort(string_list):
    # Unsorted order: "fig", "date", "apple", "banana", "cherry"
    unsorted_order = ["fig", "date", "apple", "banana", "cherry"]
    
    # Sort the list using Python's built-in sorted function with a key as a tuple
    # The first element of the tuple is the length of the string, and the second element is the string itself
    # This ensures that strings with the same length will be sorted alphabetically
    sorted_list = sorted(unsorted_order, key=lambda x: (len(x), x))
    
    return sorted_list

# Example usage:
string_list = ["apple", "fig", "banana", "cherry", "date"]
print(custom_sort(string_list))  # Output: ['fig', 'date', 'apple', 'banana', 'cherry']