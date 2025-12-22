def solve_puzzle():
    # 各家の位置を特定
    houses = ['A', 'B', 'C', 'D', 'E']
    colors = {'A': 'yellow', 'B': 'blue', 'C': 'green', 'D': 'red', 'E': 'white'}
    nationalities = {'A': 'Norway', 'B': '', 'C': '', 'D': 'England', 'E': ''}
    drinks = {'A': '', 'B': '', 'C': '', 'D': '', 'E': ''}
    cigarettes = {'A': '', 'B': '', 'C': '', 'D': '', 'E': ''}
    pets = {'A': '', 'B': '', 'C': '', 'D': '', 'E': ''}

    # 制約から直接特定できる情報を書き出し
    nationalities['A'] = 'Norway'
    nationalities['D'] = 'England'

    # 制約を組み合わせて間接的に導き出す情報を推論
    if colors['C'] == 'green':
        houses.index('C') - 1 == houses.index('B')
    if nationalities['B']:
        drink_sweden = 'coffee'
        cigarette_denmark = 'dunhill'
        pet_parrot = 'blue master'
        if colors['A'] == 'yellow':
            cigarette_germany = 'prince'
        else:
            cigarette_germany = 'blend'
    if houses.index('C') == 2:
        drink_central = 'milk'
    if houses[0] == 'red':
        nationalities['E'] = 'England'
        drink_england = 'coffee'
        cigarette_england = 'blue master'
        pet_dog = 'Sweden'
    if colors['D'] == 'red':
        drink_central = 'milk'
    if houses.index('E') == 4:
        drink_blend_neighbor = 'water'
    if nationalities['B']:
        pet_parrot = 'blue master'
        if colors['A'] == 'yellow':
            cigarette_germany = 'prince'
        else:
            cigarette_germany = 'blend'
    if houses.index('E') == 1:
        drink_horse_neighbor = 'dunhill'
    if nationalities['B']:
        drink_sweden = 'coffee'
        if colors['A'] == 'yellow':
            cigarette_germany = 'prince'
        else:
            cigarette_germany = 'blend'
    if houses.index('E') == 3:
        drink_fish = 'beer'
        nationalities['B'] = 'Germany'

    # 各属性を各家に割り当てる
    for house in houses:
        if not nationalities[house]:
            if houses.index(house) == 0:
                nationalities[house] = 'Norway'
            elif houses.index(house) == 1:
                nationalities[house] = 'Germany'
            elif houses.index(house) == 2:
                if colors['C'] == 'green':
                    nationalities[house] = 'Sweden'
                else:
                    nationalities[house] = 'Denmark'
            elif houses.index(house) == 3:
                nationalities[house] = 'England'
            elif houses.index(house) == 4:
                if colors['D'] == 'red':
                    nationalities[house] = 'England'
                else:
                    nationalities[house] = 'Denmark'
        if not drinks[house]:
            if house == 'A':
                drinks[house] = 'coffee'
            elif house == 'B':
                drinks[house] = 'beer' if nationalities[house] == 'Germany' else 'milk'
            elif house == 'C':
                drinks[house] = 'coffee' if colors['C'] == 'green' else 'tea'
            elif house == 'D':
                drinks[house] = 'milk'
            elif house == 'E':
                drinks[house] = 'beer'
        if not cigarettes[house]:
            if house == 'A':
                cigarettes[house] = 'dunhill' if colors['A'] == 'yellow' else 'prince'
            elif house == 'B':
                cigarettes[house] = 'blue master'
            elif house == 'C':
                cigarettes[house] = 'dunhill' if colors['C'] == 'green' else 'blend'
            elif house == 'D':
                cigarettes[house] = 'prince'
            elif house == 'E':
                cigarettes[house] = 'blend'
        if not pets[house]:
            if house == 'A':
                pets[house] = 'fish'
            elif house == 'B':
                pets[house] = 'dog' if nationalities[house] == 'Sweden' else 'cat'
            elif house == 'C':
                pets[house] = 'parrot' if colors['C'] == 'green' else 'horse'
            elif house == 'D':
                pets[house] = 'dog'
            elif house == 'E':
                pets[house] = 'cat'

    # 最終的な問いに答える
    for house, nationality in nationalities.items():
        if pets[house] == 'fish':
            return nationality