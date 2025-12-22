def length_sort(string_list):
  """
  Redonas novan liston kun la ĉenoj el `string_list` ordigitaj laŭ kreska ordo de ilia longeco.

  Args:
    string_list: Liston de ĉenoj.

  Returns:
    Liston de ĉenoj ordigitaj laŭ ilia longeco.
  """
  return sorted(string_list, key=len)