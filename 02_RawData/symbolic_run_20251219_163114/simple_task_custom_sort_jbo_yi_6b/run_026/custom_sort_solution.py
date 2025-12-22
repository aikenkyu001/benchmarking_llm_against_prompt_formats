def custom_sort(string_list):
    # Sorting the list in ascending order of length first, then lexicographically (alphabetically)
    return sorted(string_list, key=lambda x: (len(x), x))

# Test case
fruit_list = ["apple", "fig", "banana", "cherry", "date"]
sorted_list = custom_sort(fruit_list)
print(sorted_list)