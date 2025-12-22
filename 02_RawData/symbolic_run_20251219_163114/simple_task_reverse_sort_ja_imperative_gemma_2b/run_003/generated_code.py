def reverse_sort(number_list):
  """
   number_list の数値を降順にソートした新しいリストを返します。

  入力引数:
    number_list: 数値のリスト。

  返値:
    新しいリスト。
  """

  # number_list の要素を反転して新しいリストを作成する。
  reversed_list = sorted(number_list[::-1])

  return reversed_list