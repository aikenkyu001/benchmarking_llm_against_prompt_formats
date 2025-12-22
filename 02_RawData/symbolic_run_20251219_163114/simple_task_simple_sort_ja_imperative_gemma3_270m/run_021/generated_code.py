def simple_sort(number_list):
  """
  タスクの実行。

  Args:
    number_list: 数値リスト

  Returns:
    ソートされた新しいリスト。
  """
  try:
    sorted_list = sorted(number_list)
    return sorted_list
  except Exception as e:
    print(f"エラーが発生しました: {e}")
    return None  # または、エラーを処理する別の方法