def length_sort(string_list):
  """
  文字列のリストを、その長さが短いものから長いものへと昇順に並べ替えます。

  Args:
    string_list: 文字列のリスト。

  Returns:
    長さが短いものから長いものへと並べ替えられた新しいリスト。
  """
  return sorted(string_list, key=len)

# 例
string_list = ["apple", "banana", "kiwi", "orange"]
sorted_list = length_sort(string_list)
print(sorted_list)  # 出力: ['kiwi', 'apple', 'orange', 'banana']