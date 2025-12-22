gunma
def length_sort(string_list):
    sorted_list = []
    for string in string_list:
        sorted_list.append((len(string), string))
    sorted_list.sort()
    sorted_strings = [item[1] for item in sorted_list]
    return sorted_strings