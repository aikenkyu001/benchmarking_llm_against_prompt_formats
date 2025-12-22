def length_sort(string_list):
    # Create an empty list to store the sorted strings
    sorted_strings = []

    # Iterate through each string in the input list
    for string in string_list:
        # Append the string to the sorted list, maintaining the order of strings with the same length
        while sorted_strings and len(sorted_strings[-1]) > len(string):
            sorted_strings.pop()
        sorted_strings.append(string)

    return sorted_strings