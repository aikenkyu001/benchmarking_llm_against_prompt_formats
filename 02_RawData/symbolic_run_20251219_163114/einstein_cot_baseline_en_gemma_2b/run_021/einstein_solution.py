def solve_puzzle():
    # Identify the position of each house
    house_positions = [1, 2, 3, 4, 5]

    # Write down the information that can be directly identified from each constraint
    constraints = [
        "The Brit lives in the red house.",
        "The Swede keeps dogs as pets.",
        "The Dane drinks tea.",
        "The green house is on the left of the white house.",
        "The person who lives in the green house drinks coffee.",
        "The person who smokes Pall Mall rears birds.",
        "The owner who smokes Bluemaster drinks beer.",
        "The person who smokes Blends lives next to the one who keeps cats.",
        "The person who keeps a horse lives next to the person who smokes Dunhill.",
        "The owner who smokes Prince lives next to the one who keeps cats.",
        "The person who keeps a fish lives next to the person who smokes Dunhill.",
    ]

    # Infer information that can be derived indirectly by combining the constraints
    for i, constraint in enumerate(constraints):
        for j, position in enumerate(house_positions):
            if constraint.startswith(f"The {position} lives in the {i} house"):
                house_positions[i] = position

    # Finally, identify the person who owns the fish and state their nationality
    fish_position = house_positions[5]
    fish_owner = constraints[constraints.index("The person who keeps a fish lives next to the person who smokes Dunhill")][1]
    return fish_owner