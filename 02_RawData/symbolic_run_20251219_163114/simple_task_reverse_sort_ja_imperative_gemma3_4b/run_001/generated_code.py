def reverse_sort(number_list):
  """
  数値リストを降順にソートした新しいリストを返します。

  Args:
    number_list: 数値のリスト。

  Returns:
    数値のリストを降順にソートした新しいリスト。
  """
  sorted_list = sorted(number_list, reverse=True)
  return sorted_list

# 例
numbers = [5, 2, 8, 1, 9, 4]
sorted_numbers = reverse_sort(numbers)
print(sorted_numbers)  # 出力: [9, 8, 5, 4, 2, 1]