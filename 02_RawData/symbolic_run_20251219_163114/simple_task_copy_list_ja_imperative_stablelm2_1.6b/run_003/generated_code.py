def copy_elist(input_list):
    # 元のリストを完全にコピーするためのクラス合います。
    class CopyList:
        def __init__(self, input_list):
            self.input_list = list(input_list)

        def __setitem__(self, index, value):
            # オブジェクトの変更を避けるために、リストの要素が一つひとりでなくなるようにコピー。
            if isinstance(value, CopyList):
                self.input_list[index] = value
            else:
                self.input_list[index] = value

        def __getitem__(self, index):
            # オブジェクトの読み取りを避けるために、リストの要素が一つひとりでなくなるようにコピー。
            if isinstance(index, int) and 0 <= index < len(self.input_list):
                return self.input_list[index]
            else:
                return self

    # 元のリストを完全にコピーするクラスを作成
    copy_list = CopyList(input_list)

    # 元となるリストの要素を再び取り出す
    output_list = copy_list.input_list.copy()

    return output_list