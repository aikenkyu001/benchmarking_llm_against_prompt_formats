def custom_sort(string_list):
    # Part 1: Sort by clan name and then by individual name
    sorted_list = sorted(string_list, key=lambda x: (x.split()[0], x.split()[1]))
    
    # Part 2: If there are multiple clan names with the same individual name,
    # sort them alphabetically
    for i in range(len(sorted_list) - 1):
        if sorted_list[i].split()[0] == sorted_list[i+1].split()[0]:
            sorted_list[i:i+2] = sorted(sorted_list[i:i+2], key=lambda x: x.split()[1])
    
    return sorted_list

string_list = ["apple", "fig", "banana", "cherry", "date"]
print(custom_sort(string_list))  # Output: ["fig", "date", "apple", "banana", "cherry"]