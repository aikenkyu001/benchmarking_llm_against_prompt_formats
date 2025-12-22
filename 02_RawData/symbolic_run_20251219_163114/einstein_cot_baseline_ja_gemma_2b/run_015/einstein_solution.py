def solve_puzzle():
    # 各家の位置を特定する
    positions = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

    # 各制約から直接特定できる情報を書き出す
    for i, position in enumerate(positions):
        if i == 0 or i == 1:
            color = "red"
        elif i == 2 or i == 3:
            country = "Sweden"
        elif i == 4 or i == 5:
            drink = "coffee"
        elif i == 6:
            animal = "bird"
        elif i == 7:
            clothing = "pants"
        elif i == 8:
            food = "milk"
        elif i == 9:
            location = "Norway"
        elif i == 10:
            drink = "beer"
        elif i == 11:
            animal = "horse"
        elif i == 12:
            clothing = "suit"
        elif i == 13:
            food = "fish"

    # すべての属性が各家に割り当てられるまで、このプロセスを繰り返す
    for i, position in enumerate(positions):
        for j, property in enumerate(["color", "country", "drink", "animal", "clothing", "food", "location", "drink", "animal", "clothing", "food"]):
            if property in position[i]:
                if position[i][j] != property:
                    break
                else:
                    continue

    # 最初の属性を特定し、その国籍を結論付ける
    final_color = position[0][0]
    final_country = position[0][1]

    # 結論を標準出力に出力する
    print(f"{final_country}")