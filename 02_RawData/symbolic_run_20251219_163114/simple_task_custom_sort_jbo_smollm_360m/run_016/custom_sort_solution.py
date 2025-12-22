def sort_by_name(string_list):
    return sorted(string_list, key=lambda x: x.split(" ")[0])