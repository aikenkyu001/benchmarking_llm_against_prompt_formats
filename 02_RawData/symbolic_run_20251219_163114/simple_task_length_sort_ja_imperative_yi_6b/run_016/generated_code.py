def length_sort(string_list):
    return sorted(string_list, key=len)

# テスト用の文字列リスト
test_strings = ['apple', 'banana', 'cherry', 'date']
sorted_strings = length_sort(test_strings)
print(sorted_strings)  # ['apple', 'date', 'banana', 'cherry']