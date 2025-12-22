def simple_sort(number_list):
  """
  Simple sorting function.

  Args:
    number_list: A list of numbers.

  Returns:
    A new list with the numbers from `number_list` sorted in ascending order.
  """

  # Copy the number_list to a new list called sorted_list.
  sorted_list = copy.deepcopy(number_list)

  # Sort the sorted_list in ascending order.
  sorted_list.sort()

  # Return the sorted_list.
  return sorted_list