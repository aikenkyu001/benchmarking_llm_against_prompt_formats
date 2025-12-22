def custom_sort(string_list):
    return sorted(string_list, key=len, reverse=True) + sorted(string_list, key=lambda x: ord(x[0]) if len(x) == 1 else 0)