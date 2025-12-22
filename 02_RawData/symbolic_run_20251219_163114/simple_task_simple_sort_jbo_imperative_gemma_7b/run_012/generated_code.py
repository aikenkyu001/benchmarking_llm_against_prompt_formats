def simple_sort(number_list):
    for i in range(len(number_list) - 1):
        for j in range(i + 1, len(number_list)):
            if number_list[i] > number_list[j]:
                number_list[i], number_list[j] = number_list[j], number_list[i]
    return number_list