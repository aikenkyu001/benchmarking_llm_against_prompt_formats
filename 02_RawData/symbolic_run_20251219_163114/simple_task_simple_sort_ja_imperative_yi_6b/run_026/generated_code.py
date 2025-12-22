def simple_sort(number_list):
    return sorted(number_list)

# テスト用の数字リスト
test_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = simple_sort(test_numbers)
print(sorted_numbers)  # 出力: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]