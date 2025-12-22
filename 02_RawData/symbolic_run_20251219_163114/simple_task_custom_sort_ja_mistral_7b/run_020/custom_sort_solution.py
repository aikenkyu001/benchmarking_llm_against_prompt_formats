def custom_sort(string_list):
    return sorted(string_list, key=len) + sorted(filter(None, [x for x in string_list if len(x) == max(map(len, string_list))]), reverse=True)