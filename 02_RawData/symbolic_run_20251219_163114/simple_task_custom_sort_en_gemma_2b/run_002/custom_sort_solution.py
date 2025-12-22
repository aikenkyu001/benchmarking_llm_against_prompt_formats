def custom_sort(string_list):
    # Sort the list by length, with shorter strings coming first
    string_list.sort(key=len, reverse=True)

    # If the lengths of the strings are the same, sort them in lexicographical order
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if string_list[i] > string_list[j]:
                string_list[i], string_list[j] = string_list[j], string_list[i]

    return string_list