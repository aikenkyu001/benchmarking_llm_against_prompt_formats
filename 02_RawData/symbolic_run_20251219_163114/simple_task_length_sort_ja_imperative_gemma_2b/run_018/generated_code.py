def length_sort(string_list):
  """
  文字列の長さで降順に並べる新しいリストを返します。

  引数:
    string_list: 要処理する文字列のリスト。

  返値:
    新しい文字列のリスト。
  """

  # string_list の文字列を分割する。
  strings = string_list

  # 各文字の長さを取得する。
  lengths = [len(s) for s in strings]

  # 長さが最も短な文字のサイズを取得する。
  shortest_length = min(lengths)

  # 新しいリストを構築する。
  sorted_strings = []
  for length in lengths:
    if length == shortest_length:
      sorted_strings.append(strings.pop(0))
    else:
      sorted_strings.append(strings.pop())

  return sorted_strings