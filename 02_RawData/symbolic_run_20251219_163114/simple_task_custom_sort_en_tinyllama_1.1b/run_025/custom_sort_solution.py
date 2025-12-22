def custom_sort(string_list):
    # Define two helper functions for primary and secondary rules
    def length_ascending(a, b):
        return len(a) < len(b)
    
    def alphabetical_order(a, b):
        return cmp(a[0], b[0]) if a[0] == b[0] else cmp(a[1], b[1])
    
    # Sort the list in ascending order based on length
    sorted_list = sorted(string_list, key=lambda x: (x[0], x))
    
    # Sort the list in alphabetical order based on first character
    sorted_list.sort(key=lambda x: (len(x), x[1]))
    
    return sorted_list