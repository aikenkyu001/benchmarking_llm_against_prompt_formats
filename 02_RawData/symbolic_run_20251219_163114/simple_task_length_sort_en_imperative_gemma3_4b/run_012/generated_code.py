def length_sort(string_list):
  """
  Sorts a list of strings in ascending order based on their length.

  Args:
    string_list: A list of strings.

  Returns:
    A new list with the strings from string_list sorted in ascending order based on their length.
  """
  return sorted(string_list, key=len)