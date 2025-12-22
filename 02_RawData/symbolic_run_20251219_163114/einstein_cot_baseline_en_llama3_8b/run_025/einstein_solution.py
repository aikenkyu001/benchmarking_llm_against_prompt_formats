def solve_puzzle():
    # Step 1: Identify the position of each house (from 1st to 5th)
    houses = ['Norwegian', 'Swede', 'Danish', 'German', 'British']

    # Step 2: Write down the information that can be directly identified from each constraint
    constraints = [
        {'nationality': 'Norwegian', 'house': 1},
        {'pet': 'dogs', 'house': None},  # Swede keeps dogs as pets, but we don't know which house yet
        {'beverage': 'tea', 'house': None},  # Dane drinks tea, but we don't know which house yet
        {'color': 'green', 'left_of': 'white'},  # Green house is on the left of the white house
        {'beverage': 'coffee', 'house': None},  # Person who lives in the green house drinks coffee
        {'cigarette': 'Pall Mall', 'pet': 'birds'},  # Person who smokes Pall Mall rears birds
        {'cigarette': 'Dunhill', 'color': 'yellow'},  # Owner of the yellow house smokes Dunhill
        {'beverage': 'milk', 'house': None},  # Person living in the center house drinks milk
        {'nationality': 'German', 'cigarette': 'Prince'},  # German smokes Prince
    ]

    # Step 3: Infer information that can be derived indirectly by combining the constraints
    for constraint in constraints:
        if constraint['house'] is None:
            for i, house in enumerate(houses):
                if (constraint['nationality'] == house and
                        not any(c['nationality'] == house for c in constraints)):
                    constraint['house'] = i + 1

    # Step 4: Repeat the process until all attributes are assigned to each house
    while True:
        changed = False
        for constraint in constraints:
            if constraint['house'] is None:
                for other_constraint in constraints:
                    if (constraint != other_constraint and
                            constraint['nationality'] == other_constraint['nationality']):
                        constraint['house'] = other_constraint['house']
                        changed = True
                        break
                if changed:
                    break

        if not changed:
            break

    # Step 5: Identify the person who owns the fish and state their nationality
    for i, house in enumerate(houses):
        if (i == 0 or houses[i-1] != 'Swede') and \
           (i == len(houses) - 1 or houses[i+1] != 'German'):
            return f"{houses[i]}"