def reverse_sort(number_list):
  """
  タスクの実行。

  Args:
    number_list: 数値リスト。

  Returns:
    ソートされた新しいリスト。
  """
  sorted_list = sorted(number_list)
  return sorted_list

# 例
number_list = [5, 2, 1, 3, 4]
sorted_list = reverse_sort(number_list)
print(sorted_list)