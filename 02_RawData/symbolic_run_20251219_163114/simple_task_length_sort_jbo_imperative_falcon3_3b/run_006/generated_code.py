def length_sort(strings):
    """
    Sorts a list of strings by their lengths in ascending order.

    Parameters:
    strings (list): A list of strings to be sorted.

    Returns:
    list: The sorted list of strings based on their lengths.
    """
    return sorted(strings, key=len)

# Example usage:
string_list = ["apple", "banana", "cherry", "date"]
sorted_list = length_sort(string_list)
print(sorted_list)