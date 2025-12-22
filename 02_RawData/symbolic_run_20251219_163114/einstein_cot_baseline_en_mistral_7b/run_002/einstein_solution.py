def solve_puzzle():
    houses = ['Norwegian', 'Swede', 'Brit', 'Dane', 'German']
    colors = ['yellow', 'blue', 'red', 'white', 'green']
    beverages = ['water', 'coffee', 'milk', 'tea', 'beer']
    cigarettes = ['Blends', 'Pall Mall', 'Dunhill', 'Prince', 'Bluemaster']
    pets = ['cats', 'dogs', 'fish', 'horse', 'birds']

    # Position of houses based on given constraints
    houses[0], houses[3] = houses[3], houses[0]  # Norwegian lives next to blue house
    houses[4] = 'German'  # German smokes Prince
    colors[1], colors[2] = colors[2], colors[1]  # Green house is on the left of white house
    cigarettes[3] = 'Dunhill'  # Owner of yellow house smokes Dunhill
    pets[0], pets[4] = pets[4], pets[0]  # The person who keeps a horse lives next to the person who smokes Dunhill
    cigarettes[2] = 'Prince'  # The German smokes Prince
    beverages[3] = 'tea'  # Dane drinks tea
    houses[1], pets[1] = pets[1], houses[1]  # Swede keeps dogs as pets
    cigarettes[0] = 'Blends'  # The Brit lives in the red house and smokes a different brand than German and Norwegian
    beverages[2] = 'milk'  # Person living in the center house drinks milk
    houses[4], cigarettes[4] = cigarettes[4], houses[4]  # German smokes Bluemaster
    pets[3] = 'horse'  # Position of the horse owner derived from previous steps
    neighbors = [(0, 1), (1, 2), (2, 3), (3, 4)]  # Pair of house numbers for each neighbor relationship
    for neighbor in neighbors:
        if cigarettes[neighbor[0]] == 'Blends':
            pets[neighbor[1]] = 'cats'  # The person who smokes Blends lives next to the one who keeps cats
        elif pets[neighbor[1]] == 'horse':
            beverages[neighbor[0]] = 'water'  # The person who smokes Blends has a neighbor who drinks water

    # Final answer: Who owns the fish?
    for i, house in enumerate(houses):
        if pets[i] == 'fish':
            return f"{house}"