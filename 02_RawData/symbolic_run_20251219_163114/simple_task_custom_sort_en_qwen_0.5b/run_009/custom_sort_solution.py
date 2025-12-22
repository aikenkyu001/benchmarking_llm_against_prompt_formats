def custom_sort(string_list):
    # Sort the list by length
    string_list.sort(key=len, reverse=True))
    
    return string_list

# Example usage
string_list = ["apple", "fig", "banana", "cherry", "date"]
sorted_string_list = custom_sort(string_list)
print(sorted_string_list)  # Output: ['fig', 'date', 'apple', 'banana', 'cherry']]