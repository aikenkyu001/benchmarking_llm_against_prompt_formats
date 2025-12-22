def copy_list(input_list):
    """Kopira listu."""
    output_list = []
    for item in input_list:
        output_list.append(item.copy())
    return output_list