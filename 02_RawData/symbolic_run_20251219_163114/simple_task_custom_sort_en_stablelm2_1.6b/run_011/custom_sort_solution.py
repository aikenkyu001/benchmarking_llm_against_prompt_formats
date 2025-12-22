def custom_ sort(string_list):
    string_list.sort(key=lambda x: (len(x), x))
    return string_list

# Test the function with example input
print(custom_sort(["apple", "fig", "banana", "cherry", "date"]))