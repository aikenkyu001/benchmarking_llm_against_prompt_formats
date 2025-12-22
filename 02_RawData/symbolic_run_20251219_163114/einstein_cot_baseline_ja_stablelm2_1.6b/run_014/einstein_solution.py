def solve_puzzle():
    # イギリス人とスウェデン人が住む家を特定
    german_house = 1
    sweden_house = 2

    # ステップ1から2までの情報を統合
    for i in range(3, 5):
        if i % 2 == 0:
            # イギリス人とスウェデン人が異なる銘柄のタバコを吸っている
            german_house = i
        else:
            # ステップ1から2までの情報を統合
            if sweden_house % 2 == ..
                # イギリス人とスウェデン人が中央家に住んでいることを示しています
                german_house = 5

    # 中央家の持ち主が紅茶を飲むという制約条件がある
    if sweden_house % 2 == 0:
        # スウェデン人（2番目）が中央家に住んでいることを示しています
        return "Swedish"
    else:
        # イギリス人（1番目）とスウェデン人（2番目）が異なる銘柄のタバコを吸っている
        return "German"

# パズル解決
puzzle = solve_puzzle()
print("The answer is:", puzzle)