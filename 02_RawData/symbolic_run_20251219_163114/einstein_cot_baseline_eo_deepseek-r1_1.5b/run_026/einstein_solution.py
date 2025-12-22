def solve_puzzle():
    # Identigas la posicion de la fiŝo en la vico
    domo_posiciones = {
        1: 'ruĝa', 
        2: 'Svedo',
        3: 'Dano',
        4: 'verda',
        5: 'bloka'
    }
    
    # Identigas la naciecon de la fiŝon
    nacio_de_fisico = {
        'ruĝa': 'akvon',
        'Svedo': 'bieron',
        'Dano': 'lakton',
        'verda': 'lakton',
        'bloka': 'akvon'
    }
    
    # Konkludas la naciecon de la fiŝon
    return nacio_de_fisico['ruĝa']