def simple_sort(number_list):
    sorted_list = []
    while number_list:
        min_value = min(number_list)
        number_list.remove(min_value)
        sorted_list.append(min_value)
    return sorted_list