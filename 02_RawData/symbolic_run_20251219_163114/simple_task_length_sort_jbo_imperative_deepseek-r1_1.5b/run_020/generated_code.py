def length_sort(lst):
    return " ".join(sorted(lst, key=len))

strings = ["banana", "apple", "cherry"]
sorted_strings = length_sort(strings)
print("Sorted by length:", sorted_strings)

class JONAI:
    def __init__(self, strings=None):
        self.sorted_list = []
        if strings is not None:
            self.sorted_list = sorted(strings, key=lambda x: len(x))
    
    def length_sort(self, lst):
        return " ".join(sorted(lst, key=len))
    
    def string_list(self):
        return self.sorted_list

joni = JONAI()
sorted_strings_joni = length_sort(joni.sorted_list)
print("Sorted by length:", sorted_strings_joni)