def length_sort(string_list):
    sorted_string_list = []
    
    for string in string_list:
        if len(sorted_string_list) < len(string):
            sorted_string_list.append(string)
        
    return sorted_string_list

# Example usage
string_list = ["apple", "banana", "cherry"],
sorted_string_list = length_sort(string_list))
print(sorted_string_list)