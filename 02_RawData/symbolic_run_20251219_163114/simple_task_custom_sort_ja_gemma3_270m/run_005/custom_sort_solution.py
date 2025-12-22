def custom_sort(string_list):
    """
    リストをカスタムソートする関数。

    Args:
        string_list: 必須の文字列のリスト。

    Returns:
        ソートされたリスト。
    """
    try:
        sorted_list = sorted(string_list)
        return sorted_list
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return []