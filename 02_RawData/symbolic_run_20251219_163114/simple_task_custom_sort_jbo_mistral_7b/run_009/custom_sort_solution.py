def custom_sort(string_list):
    def reverse(x, y):
        return (y[0] < x[0]) - (x[0] < y[0])  # reverse sort for minus sign

    def natural(x, y):
        return cmp(x[0], y[0])               # natural sort for no sign

    string_list = [(len(s), s) for s in string_list]
    string_list.sort(reverse=True)            # reverse sort by length first
    string_list.sort(key=natural)             # then sort lexicographically (alphabetically)
    result = [s[1] for s in string_list]      # extract sorted strings from the list of tuples
    return result