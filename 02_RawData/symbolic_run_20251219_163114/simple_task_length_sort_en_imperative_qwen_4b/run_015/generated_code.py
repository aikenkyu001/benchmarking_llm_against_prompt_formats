def length_sort(string_list):
    # Create an empty list to store the sorted strings
    sorted_strings = []

    # Iterate through each string in the input list
    for string in string_list:
        # Calculate the length of the current string
        length = len(string)

        # Add the current string to the sorted list if its length is greater than or equal to the length of the last string added to the sorted list
        if length >= sorted_strings[-1]].append(string)
    return sorted_strings