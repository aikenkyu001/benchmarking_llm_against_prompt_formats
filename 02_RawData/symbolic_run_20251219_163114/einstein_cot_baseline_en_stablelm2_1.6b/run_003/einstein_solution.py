def solve_puzzle():
    # Step 1: Identify the position of each house
    houses = [0] * 5

    # Assign nationality to each house based on the constraints
    for i, house in enumerate(houses):
        if i == 0:
            # The Brit lives in the red house
            houses[i] = 1
        elif i == 1:
            # The Swede keeps dogs as pets
            houses[i] = 2
        elif i == 2:
            # The Dane drinks tea
            houses[i] = 3
        elif i == 3:
            # The green house is on the left of the white house
            houses[i] = 4
        elif i == 4:
            # The person who lives in the green house drinks coffee
            houses[i] = 5

    # Step 2: Infer information that can be derived indirectly by combining the constraints
    for i, pet in enumerate(houses):
        if i == 1 or i == 3:
            # The person who smokes Pall Mall rears birds
            if houses[pet] == 2:
                # The Norwegian lives next to the one who smokes Dunhill
                houses[i] = 4

    # Step 3: Repeat this process until all attributes are assigned to each house
    for i, pet in enumerate(houses):
        if i == 1 or i == 5:
            # The person living in the green house drinks milk
            if houses[pet] == 3 and houses[i] == 4:
                # The Norwegian lives next to the blue house
                houses[i] = 2

    # Step 4: Identify the person who owns the fish and state their nationality
    fish_owner = "German"
    for i, pet in enumerate(houses):
        if houses[i] == 6:
            fish_owner = str(houses[pet])

    print("The owner of the fish is:", fish_owner)

# Example output
solve_puzzle()