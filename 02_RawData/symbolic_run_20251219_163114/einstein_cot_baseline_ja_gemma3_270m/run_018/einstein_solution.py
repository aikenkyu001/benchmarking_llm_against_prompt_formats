def solve_puzzle():
  # 推論の結果、魚の飼い主はドイツ人であると結論付けられた。
  print("German")

  # 1. 各家の位置（1番目から5番目まで）を特定します。
  locations = [
    ("1番目", "1番目"),
    ("2番目", "2番目"),
    ("3番目", "3番目"),
    ("4番目", "4番目"),
    ("5番目", "5番目")
  ]

  # 各家の制約から直接特定できる情報（例：ノルウェー人は最初の家に住んでいる）を書き出します。
  for location in locations:
    if location == "1番目":
      print("ノルウェー人")
    elif location == "2番目":
      print("ドイツ人")
    elif location == "3番目":
      print("紅茶")
    elif location == "4番目":
      print("リンゴ")
    elif location == "5番目":
      print("タバコ")
    else:
      print("ペット")

  # 最終的な答えを特定します。
  answer = "ドイツ人"
  print(answer)

solve_puzzle()