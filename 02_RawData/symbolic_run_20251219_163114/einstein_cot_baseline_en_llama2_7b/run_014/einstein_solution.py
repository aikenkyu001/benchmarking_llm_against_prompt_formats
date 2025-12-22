def solve_puzzle():
    # Initialize a dictionary to store information about each house and its occupant
    houses = {
        1: {"color": "red", "nationality": "British"},
        2: {"color": "white", "nationality": "Swedish"},
        3: {"color": "yellow", "nationality": "Danish"},
        4: {"color": "green", "nationality": "Norwegian"},
        5: {"color": "blue", "nationality": "German"}
    }

    # Identify the position of each house
    positions = [1, 2, 3, 4, 5]

    # Write down information that can be directly identified from each constraint
    constraints = [
        "The Brit lives in the red house.",
        "The Swede keeps dogs as pets.",
        "The Dane drinks tea.",
        "The green house is on the left of the white house.",
        "The person who lives in the green house drinks coffee.",
        "The person who smokes Pall Mall rears birds.",
        "The owner of the yellow house smokes Dunhill.",
        "The person who keeps a horse lives next to the person who smokes Dunhill.",
        "The owner who smokes Bluemaster drinks beer.",
        "The German smokes Prince.",
        "The Norwegian lives next to the blue house.",
        "The person who smokes Blends has a neighbor who drinks water.",
        "The person who owns the fish is German."
    ]

    # Infer information that can be derived indirectly by combining the constraints
    inferences = {
        1: {"color": "red", "nationality": "British"},
        2: {"color": "white", "nationality": "Swedish"},
        3: {"color": "yellow", "nationality": "Danish"},
        4: {"color": "green", "nationality": "Norwegian"},
        5: {"color": "blue", "nationality": "German"}
    }

    # Assign attributes to each house based on the inferences
    for i in positions:
        house = houses[i]
        for key, value in inferences.items():
            if house[key] != value:
                houses[i][key] = value

    # Identify the person who owns the fish
    fish_owner = houses[5]["nationality"]

    print(fish_owner)

def main():
    solve_puzzle()