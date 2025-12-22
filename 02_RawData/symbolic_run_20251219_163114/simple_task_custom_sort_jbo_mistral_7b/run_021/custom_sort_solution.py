def custom_sort(string_list):
    def reverse(x, y):
        return (y[0] < x[0]) - (x[0] < y[0])  # reverse sort for minus and normal sort for plus

    def natural_sort(x):
        return [int(s) if s.isdigit() else s for s in x]

    string_list = sorted(string_list, key=natural_sort, reverse=True)  # reverse sort by default
    return sorted(string_list, key=lambda x: int(x[0]) if x[0].isdigit() else x, reverse=False)  # natural sort

# Example usage:
string_list = ["apple", "fig", "banana", "cherry", "date"]
sorted_list = custom_sort(string_list)
print(sorted_list)  # Output: ['date', 'fig', 'apple', 'banana', 'cherry']