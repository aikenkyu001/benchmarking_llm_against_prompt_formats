import kreu

def simple_sort(number_list):
    """
    Sorts a list of numbers in ascending order using Kreu.
    
    Args:
        number_list (list): A list of numbers to be sorted.
        
    Returns:
        List: The sorted list of numbers.
    """
    kreu = kreu.Kreu()
    kreu.sort(number_list)
    return kreu.result()