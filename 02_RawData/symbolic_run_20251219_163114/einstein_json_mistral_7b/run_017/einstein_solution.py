def solve_puzzle():
    houses = {'Red': None, 'Green': None, 'White': None, 'Yellow': None, 'Blue': None}
    pets = {'Dog': None, 'Bird': None, 'Cat': None, 'Horse': None, 'Fish': None}
    nationalities = {'Brit': None, 'Swede': None, 'Dane': None, 'Norwegian': None, 'German': None}
    drinks = {'Tea': None, 'Coffee': None, 'Milk': None, 'Beer': None, 'Water': None}
    smokes = {'Pall Mall': None, 'Dunhill': None, 'Blends': None, 'Bluemaster': None, 'Prince': None}

    for constraint in data['constraints']:
        if constraint['type'] == "association":
            subject = constraint['subject']
            object_ = constraint['object']
            nationalities[list(subject.keys())[0]] = list(subject.values())[0]
            pets[list(object_.keys())[0]] = list(object_.values())[0] if 'pet' in object_ else None
            drinks[list(object_.keys())[0]] = list(object_.values())[0] if 'drink' in object_ else None
            smokes[list(object_.keys())[0]] = list(object_.values())[0] if 'smoke' in object_ else None
        elif constraint['type'] == "positional":
            subject = constraint['subject']
            houses[list(subject.keys())[0]] = list(subject.values())[0]

    for house, color in houses.items():
        if color:
            if color not in houses:
                houses[color] = None
            houses[color]['left_of'] = houses.get((houses[color]['is_left_of'] if houses[color]['is_left_of'] else 'Red')[:-1])
    for smoke, pet in smokes.items():
        if pet:
            pets[pet]['smoke'] = smoke
    for house_number, drink in houses.items():
        if drink:
            drinks[drink] = {'house_number': int(house_number)}
    for nationality, house_number in nationalities.items():
        if house_number:
            houses[house_number]['nationality'] = nationality

    answer = next((nationality for nationality, pet in pets.items() if pet == 'Fish'), None)
    print(answer)