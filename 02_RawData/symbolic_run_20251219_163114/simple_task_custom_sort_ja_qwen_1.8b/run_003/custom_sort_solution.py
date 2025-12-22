def custom_sort(lst):
    return sorted(lst, key=lambda x: len(x), reverse=True))

# Example usage:
lst = ["apple", "fig", "banana", "cherry", "date"],
sorted_lst = custom_sort(lst)

print(sorted_lst)