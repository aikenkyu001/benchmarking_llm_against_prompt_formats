def custom_sort(string_list):
    """
    Sorts a list of strings based on their first letter and then alphabetically.
    
    Args:
        string_list (list): A list of strings to be sorted.
    
    Returns:
        list: The sorted list of strings.
    """
    # Use the built-in sorted function with a custom key
    return sorted(string_list, key=lambda x: (x[0].lower(), x))

# Test the function
string_list = ["apple", "fig", "banana", "cherry", "date"]
sorted_list = custom_sort(string_list)

print("Sorted List:", sorted_list)