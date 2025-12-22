def copy_list(input_list):
    """
    Funsi ya kuibadilisha listi iliyotolewa kwenye mwelekeo mwingine.

    Args:
        input_list (list): Listi inayopewa kama input.

    Returns:
        list: Listi iliyobadilishwa.
    """
    # Kwanza, tunabadilisha listi katika mwelekeo mwingine
    output_list = input_list.copy()
    
    # Tunatoa listi iliyobadilishwa kama output
    return output_list

# Uchunguzi wa kutumia funsi hii:
if __name__ == "__main__":
    # Tunaangazia listi ya awali
    input_list = [1, 2, 3, 4, 5]
    
    # Tunatumia funsi kuibadilisha listi katika mwelekeo mwingine
    output_list = copy_list(input_list)
    
    # Tunaangazia listi iliyobadilishwa
    print("Listi iliyobadilishwa:", output_list)