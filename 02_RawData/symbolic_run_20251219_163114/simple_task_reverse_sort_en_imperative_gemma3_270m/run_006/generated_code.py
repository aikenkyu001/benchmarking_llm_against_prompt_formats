def reverse_sort(number_list):
  """
  Reverses the order of numbers in a list and returns a new list.

  Args:
    number_list: A list of numbers.

  Returns:
    A new list with the numbers from number_list sorted in descending order.
  """
  sorted_list = sorted(number_list)
  return sorted_list

# Example usage:
numbers = [5, 2, 1, 3, 4]
reversed_numbers = reverse_sort(numbers)
print(reversed_numbers)