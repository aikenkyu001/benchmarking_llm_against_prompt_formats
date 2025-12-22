def copy_list(input_list):
  """
  Creates an exact copy of a list.

  Args:
    input_list: The list to be copied.

  Returns:
    An exact copy of the input list.
  """
  try:
    return input_list.copy()
  except Exception as e:
    print(f"Error copying list: {e}")
    return input_list  # Return the original list unchanged