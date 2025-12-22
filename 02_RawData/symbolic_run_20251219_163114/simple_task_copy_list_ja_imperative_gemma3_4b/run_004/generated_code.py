def copy_list(input_list):
  """
  input_list の完全なコピーを返します。元のリストは変更してはなりません。

  Args:
    input_list: コピーするリスト。

  Returns:
    input_list のコピー。
  """
  return input_list[:]  # スライスを使ってコピーを作成
  # または
  # return input_list.copy()