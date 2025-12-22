def custom_sort(string_list):
    string_list.sort(key=len)
    string_list.sort(reverse=True, key=lambda x: x if x else -1)
    return string_list