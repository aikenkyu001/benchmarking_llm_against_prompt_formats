def length_sort(string_list):
    """Sortuje string-arrayon per longigo de iliaj elementoj"""
    return sorted(string_list, key=len)

# Testo funkciojn
if __name__ == "__main__":
    testuj = ["apple", "banana", "cherry"]
    print("Original Array:", testuj)
    print("Sorted Array (by length):", length_sort(testuj))