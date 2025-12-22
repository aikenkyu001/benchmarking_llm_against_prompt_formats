def length_sort(string_list):
    # Create an empty dictionary to store the strings and their lengths
    string_dict = {len(s): s for s in string_list}

    # Sort the keys of the dictionary (lengths) in ascending order
    sorted_keys = sorted(string_dict.keys())

    # Create a new list by iterating through the sorted keys and getting the corresponding values from the dictionary
    sorted_strings = [string_dict[key] for key in sorted_keys]

    return sorted_strings