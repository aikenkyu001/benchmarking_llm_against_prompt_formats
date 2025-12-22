def custom_sort(string_list):
    return sorted(string_list, key=lambda x: (-len(x), x))