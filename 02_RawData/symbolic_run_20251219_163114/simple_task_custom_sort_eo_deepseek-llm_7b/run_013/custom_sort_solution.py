def custom_sort(string_list):
    return sorted(string_list, key=lambda x: (len(x), x))

# Test the function
string_list = ["apple", "fig", "banana", "cherry", "date"]
sorted_list = custom_sort(string_list)
print(sorted_list)  # Output: ['fig', 'date', 'apple', 'banana', 'cherry']