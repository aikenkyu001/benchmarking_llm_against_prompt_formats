def custom_sort(string_list):
    # Unua Regulo
    if len(string_list) == 1:
        return string_list

    # Dua Regulo
    else:
        sorted_list = sorted(string_list, key=len)))
        return sorted_list

# Ekzempla Enigo
string_list = ["apple", "fig", "banana", "cherry", "date"]]

sorted_list = custom_sort(string_list)

print(sorted_list)