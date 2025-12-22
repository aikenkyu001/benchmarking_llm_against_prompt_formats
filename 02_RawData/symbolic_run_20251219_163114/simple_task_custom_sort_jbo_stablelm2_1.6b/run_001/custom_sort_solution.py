def custom_sort(string_list):
    # Sort the list using the custom key function
    sorted_list = sorted(string_list, key=lambda x: (x[0], x))
    
    return sorted_list

# Example usage:
string_list = ["John", "Alice", "Bob", "Charlie"]
sorted_result = custom_sort(string_list)
print(sorted_result)  # Output: ['Alice', 'Bob', 'Charlie', 'John']