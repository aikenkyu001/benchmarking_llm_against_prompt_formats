def simple_sort(number_list):
  """
  Sorts a list of numbers in ascending order.

  Args:
    number_list: A list of numbers.

  Returns:
    A new list with the numbers from number_list sorted in ascending order.
  """
  try:
    sorted_list = sorted(number_list)
    return sorted_list
  except Exception as e:
    print(f"Error sorting the list: {e}")
    return number_list  # Return the original list if an error occurs