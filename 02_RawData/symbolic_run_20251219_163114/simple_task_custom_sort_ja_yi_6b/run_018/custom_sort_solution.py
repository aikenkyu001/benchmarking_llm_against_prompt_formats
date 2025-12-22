def custom_sort(string_list):
    return sorted(string_list, key=lambda s: (len(s), s))

# Example usage
string_list = ["apple", "fig", "banana", "cherry", "date"]
print(custom_sort(string_list))