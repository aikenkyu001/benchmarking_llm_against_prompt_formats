def length_sort(string_list):
    sorted_list = sorted(string_list, key=lambda x: len(x))
    return sorted_list