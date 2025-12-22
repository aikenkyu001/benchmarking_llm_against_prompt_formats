def custom_sort(string_list):
    primary_rule = len(string_list) > 0
    secondary_rule = len(string_list) == 1 and primary_rule

    # Sort by Primary Rule
    string_list.sort(key=lambda x: x[primary_rule]], reverse=secondary_rule)

    return string_list


# Example usage
string_list = ["apple", "fig", "banana",  "cherry",  "date"]]

sorted_string_list = custom_sort(string_list))

print(sorted_string_list)