def length_sort(string_list):
    """
    string_listの文字列を、長さが短いものから長いものへと昇順に並べ替える。

    Args:
        string_list (list): 文字列のリスト

    Returns:
        list: 長さが短いものから長いものへと昇順に並べ替えた新しいリスト
    """
    # 1つの文字列を長さと文字列のペアでリスト化する
    length_string_pairs = [(len(s), s) for s in string_list]
    
    # 長さが短いものから長いものへと昇順に並べ替える
    sorted_length_string_pairs = sorted(length_string_pairs)
    
    # 1つの文字列をリスト化する
    sorted_string_list = [s for _, s in sorted_length_string_pairs]
    
    return sorted_string_list