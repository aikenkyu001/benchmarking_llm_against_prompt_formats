def custom_sort(string_list):
    # Sort the list in reverse order
    string_list.sort(reverse=True)

    # Return the sorted list
    return string_list


# Get the input list from the user
input_list = input("Enter a list of strings, separated by commas: ")

# Convert the input list to a list of strings
string_list = input_list.split(",")

# Sort the list of strings
sorted_list = custom_sort(string_list)

# Print the sorted list
print(sorted_list)