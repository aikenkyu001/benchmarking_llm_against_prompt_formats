def copy_list(input_list):
  """
  タスクの実行。
  入力リストの完全なコピーを返します。
  """
  try:
    copied_list = input_list.copy()  # 変更をせずにコピー
    return copied_list
  except Exception as e:
    print(f"エラーが発生しました: {e}")
    return input_list  # 戻り値は変更されたリストを返す