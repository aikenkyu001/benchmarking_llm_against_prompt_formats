def custom_sort(string_list):
    sorted_list = []

    for string in string_list:
        if len(string) > 0 and len(string) < 100:
            sorted_list.append(string)

    return sorted_list