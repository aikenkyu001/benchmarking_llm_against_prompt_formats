def length_sort(string_list):
  """
  Sorts a list of strings in ascending order based on their length.

  Args:
    string_list: A list of strings.

  Returns:
    A new list with the strings from `string_list` sorted in ascending order based on their length.
  """

  # Create a new list to store the sorted strings.
  sorted_string_list = []

  # Iterate over the strings in `string_list`.
  for string in string_list:
    # Get the length of the string.
    length = len(string)

    # Add the string to the sorted_string_list with its length.
    sorted_string_list.append((length, string))

  # Sort the sorted_string_list by length in ascending order.
  sorted_string_list.sort(key=lambda item: item[0])

  # Return the sorted list.
  return sorted_string_list