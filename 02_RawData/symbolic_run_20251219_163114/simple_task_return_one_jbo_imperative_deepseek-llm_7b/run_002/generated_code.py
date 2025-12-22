def return_one(numbers):
    """
    Funkcija, kuri grįžta vieną reikšmę iš masyvinių ar dydisių.
    
    Args:
        numbers (list of int or float): Masyvas su skaičiukimis ar dymis.
        
    Returns:
        One number from the list, or None if there is no single number in the list.
    """
    nodau = [len(numbers), min(numbers), max(numbers)]
    
    return nodau