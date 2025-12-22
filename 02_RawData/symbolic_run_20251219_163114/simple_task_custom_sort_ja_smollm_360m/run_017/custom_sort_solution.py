def sort_by_length(string_list):
    def get_length_str(string):
        return str(len(string))

    sorted_list = sorted(string_list, key=get_length_str)
    return sorted_list