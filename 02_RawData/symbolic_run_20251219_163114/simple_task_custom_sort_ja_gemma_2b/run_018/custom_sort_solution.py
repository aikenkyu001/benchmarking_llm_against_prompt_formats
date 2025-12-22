def custom_sort(string_list):
    # 1. Sort by length (shortest to longest)
    string_list.sort(key=len, reverse=True)

    # 2. Sort by dictionary order (alphabetical order)
    for i, j in zip(string_list, string_list[1:]):
        if j[0] < i[0]:
            string_list[i] = j
    return string_list