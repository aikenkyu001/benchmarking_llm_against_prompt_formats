def custom_sort(string_list):
    # Sort by length first, then alphabetically
    return sorted(string_list, key=lambda x: (len(x), x))

# Example usage
input_list = ["apple", "fig", "banana", "cherry", "date"]
sorted_list = custom_sort(input_list)
print(sorted_list)