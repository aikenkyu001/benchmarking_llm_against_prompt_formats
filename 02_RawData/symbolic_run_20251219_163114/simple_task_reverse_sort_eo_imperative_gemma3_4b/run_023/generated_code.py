def reverse_sort(number_list):
  """Redonas novan liston kun la nombroj el `number_list` ordigitaj laŭ malkreska ordo.

  Args:
    number_list: La liston de nombroj, kiun oni volas ordigi.

  Returns:
    Novan liston kun la nombroj el `number_list` ordigitaj laŭ malkreska ordo.
  """
  sorted_list = sorted(number_list, reverse=True)
  return sorted_list