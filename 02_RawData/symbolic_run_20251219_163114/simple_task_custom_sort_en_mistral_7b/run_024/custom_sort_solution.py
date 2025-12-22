def custom_sort(string_list):
    return sorted(string_list, key=len) + sorted(set(string_list) - set(sorted(string_list, key=len)), reverse=True)

# Example usage:
string_list = ["apple", "fig", "banana", "cherry", "date"]
print(custom_sort(string_list))  # Output: ['fig', 'date', 'apple', 'banana', 'cherry']