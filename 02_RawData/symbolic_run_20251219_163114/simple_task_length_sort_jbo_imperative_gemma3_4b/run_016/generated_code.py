def length_sort(string_list):
  """
  Sortuje seznam řetězců podle jejich délky.

  Args:
    string_list: Seznam řetězců.

  Returns:
    Seznam řetězců seřazený podle délky.
  """
  return sorted(string_list, key=len)