def reverse_sort(number_list):
  """
  Returns a new list with the numbers from number_list sorted in descending order.

  Args:
    number_list: A list of numbers.

  Returns:
    A new list with the numbers from number_list sorted in descending order.
  """
  new_list = sorted(number_list, reverse=True)
  return new_list