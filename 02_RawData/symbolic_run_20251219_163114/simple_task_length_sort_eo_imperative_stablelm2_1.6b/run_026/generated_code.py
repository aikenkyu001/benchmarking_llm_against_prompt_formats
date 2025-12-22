def length_sort(string_1_list):
    # Sort the list by length, in descending order
    string_1_list.sort(key=lambda x: len(x), reverse=True)
    
    return string_1_list