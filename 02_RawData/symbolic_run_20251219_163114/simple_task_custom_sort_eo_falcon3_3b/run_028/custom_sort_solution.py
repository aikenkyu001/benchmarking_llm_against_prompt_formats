def custom_sort(string_list):
    return sorted(string_list, key=lambda x: (len(x), x))

# Example usage
example_list = ["fig", "date", "apple", "banana", "cherry"]
sorted_list = custom_sort(example_list)
print(sorted_list)