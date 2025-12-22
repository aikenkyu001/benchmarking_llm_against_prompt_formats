def custom_sort(string_list):
    string_list.sort(key=lambda x: (x[1], x[0]))
    return string_list

# Sample list to sort
list1 = ["apple", "fig", "banana", "cherry", "date"]

# Sort the list using the custom_sort function
sorted_list = custom_sort(list1)

# Print the sorted list
print(sorted_list)