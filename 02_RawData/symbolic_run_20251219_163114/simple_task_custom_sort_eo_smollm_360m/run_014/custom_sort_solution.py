def custom_sort(string_list):
    def custom_key(string):
        return len(string)

    sorted_list = sorted(string_list, key=custom_key)
    return sorted_list