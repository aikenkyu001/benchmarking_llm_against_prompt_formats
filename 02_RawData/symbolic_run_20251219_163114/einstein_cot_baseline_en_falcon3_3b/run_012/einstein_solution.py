def solve_puzzle():
    # Houses are indexed from 0 to 4 for simplicity in logic
    houses = ['House 1', 'House 2', 'House 3', 'House 4', 'House 5']
    nationalities = ['Norwegian', 'Swedish', 'Dane', 'Brit', 'German']
    beverages = ['Coffee', 'Tea', 'Milk', 'Water', 'Beer']
    cigarettes = ['Dunhill', 'Prince', 'Blends', 'Pall Mall', 'Bluemaster']
    pets = ['Birds', 'Cats', 'Dogs', 'Horse', 'Fish']
    
    # Initialize assignments based on given constraints
    assignments = {
        'nationality': nationalities,
        'beverage': beverages,
        'cigarette': cigarettes,
        'pet': pets
    }
    
    # Constraints
    constraints = [
        (1, 'red'),  # Brit lives in the red house
        (0, 'Norwegian'),  # Norwegian lives in the first house
        (3, 'Dane'),  # Dane drinks tea
        (4, 'green'),  # Green house is on the left of the white house
        (5, 'coffee'),  # Person who drinks coffee lives in the green house
        (2, 'Dunhill'),  # Owner of the yellow house smokes Dunhill
        (3, 'Prince'),  # German smokes Prince
        (4, 'Blends'),  # Person who smokes Blends has a neighbor who drinks water
        (1, 'Cats'),  # Neighbor of person who smokes Blends keeps cats
        (0, 'Dogs'),  # Person who keeps dogs lives in the second house
        (3, 'Horse'),  # Person who keeps a horse lives next to the one who smokes Dunhill
        (4, 'Beer')  # Person who drinks beer has a neighbor who smokes Bluemaster
    ]
    
    # Iterate through constraints and update assignments
    for constraint in constraints:
        house_idx, attribute = constraint
        value = assignments[attribute][0]
        if house_idx not in assignments:
            assignments['house {}'.format(house_idx)] = value
    
    # Find the person who owns the fish
    for i in range(5):
        if assignments['pet'][i] == 'Fish':
            print(assignments['nationality'][i])
            break