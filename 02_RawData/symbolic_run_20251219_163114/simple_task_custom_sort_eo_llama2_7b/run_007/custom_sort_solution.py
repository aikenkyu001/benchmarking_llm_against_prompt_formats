def custom_sort(string_list):
    # Sort the list based on the length of each string
    sorted_list = [x for x in string_list if len(x) > 5]
    # Alphabetize the list
    sorted_list.sort()
    return sorted_list