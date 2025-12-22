def copy_list(input_list):
  """
  入力引数: `input_list` の完全なコピーを返せ。元のリストは変更してはならない。

  引数:
    input_list: 要素のリスト。

  返り:
    完全なコピーのリスト。
  """

  # 新しいリストを生成する
  output_list = input_list.copy()

  # 新しいリストの要素を元のリストの要素にコピーする
  for i, element in enumerate(input_list):
    output_list[i] = element

  # 新しいリストを返す
  return output_list