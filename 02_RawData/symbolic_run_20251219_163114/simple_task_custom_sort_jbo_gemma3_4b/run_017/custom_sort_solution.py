def custom_sort(string_list):
  """
  Sorts a list of strings based on the second letter of each string.
  If strings have the same second letter, they are sorted alphabetically.
  """
  return sorted(string_list, key=lambda x: (x[1], x))

# Example usage:
string_list = ["apple", "fig", "banana", "cherry", "date"]
sorted_list = custom_sort(string_list)
print(sorted_list)