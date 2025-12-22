def solve_puzzle():
    # All possible items for each category
    nationalities = ["Brit", "Swede", "Dane", "Norwegian", "German"]
    colors = ["Red", "Green", "White", "Yellow", "Blue"]
    drinks = ["Tea", "Coffee", "Milk", "Beer", "Water"]
    smokes = ["Pall Mall", "Dunhill", "Blends", "Bluemaster", "Prince"]
    pets = ["Dog", "Bird", "Cat", "Horse", "Fish"]

    # This list will hold the solution, where each index is a house (0-indexed)
    solution = [{} for _ in range(5)]

    # Keep track of used items to ensure each is used only once
    used = {
        "nationality": set(),
        "color": set(),
        "drink": set(),
        "smokes": set(),
        "pet": set()
    }

    def solve(house_index):
        # Base case: if we have filled all houses, check if the solution is valid
        if house_index == 5:
            # Constraint 14: The Norwegian lives next to the Blue house.
            if not (solution[0]["nationality"] == "Norwegian" and solution[house_index - 1]["color"] == "Blue"):
                return False
            # Constraint 15: The man who smokes Blends has a neighbor who drinks Water.
            if not (solution[house_index - 2]["smokes"] == "Blends" and solution[house_index - 1]["drink"] == "Water"):
                return False
            # Constraint 10: The man who smokes Blends lives next to the one who keeps Cats.
            if solution[house_index - 2]["smokes"] != "Blends" or solution[house_index - 1]["pet"] != "Cat":
                return False
            # Constraint 11: The man who keeps Horses lives next to the man who smokes Dunhill.
            if solution[house_index - 2]["pet"] != "Horse" or solution[house_index - 1]["smokes"] != "Dunhill":
                return False
            # Constraint 8: The man living in the center house drinks Milk.
            if house_index == 3 and solution[house_index]["drink"] != "Milk":
                return False
            # Constraint 7: The owner of the Yellow house smokes Dunhill.
            if solution[house_index - 1]["color"] == "Yellow" and solution[house_index - 1]["smokes"] != "Dunhill":
                return False
            # Constraint 6: The person who smokes Pall Mall rears Birds.
            if solution[house_index - 2]["smokes"] == "Pall Mall" and solution[house_index - 2]["pet"] != "Bird":
                return False
            # Constraint 5: The Green house's owner drinks Coffee.
            if solution[house_index - 1]["color"] == "Green" and solution[house_index - 1]["drink"] != "Coffee":
                return False
            # Constraint 4: The Green house is on the left of the White house.
            if solution[house_index - 2]["color"] != "Green" or solution[house_index - 3]["color"] != "White" or \
                    (solution[house_index - 2]["color"] == "Green" and solution[house_index - 1]["color"] != "White"):
                return False
            # Constraint 3: The Dane drinks Tea.
            if solution[house_index]["nationality"] == "Dane" and solution[house_index]["drink"] != "Tea":
                return False
            # Constraint 2: The Swede keeps Dogs as pets.
            if solution[house_index]["nationality"] == "Swede" and solution[house_index]["pet"] != "Dog":
                return False
            # Constraint 1: The Brit lives in the Red house.
            if solution[house_index]["nationality"] != "Brit" or solution[house_index]["color"] != "Red":
                return False
            # Constraint 9: The Norwegian lives in the first house.
            if house_index == 1 and solution[house_index]["nationality"] != "Norwegian":
                return False
            # Constraint 13: The German smokes Prince.
            if solution[house_index]["nationality"] == "German" and solution[house_index]["smokes"] != "Prince":
                return False
            # Constraint 12: The owner who smokes Bluemaster drinks Beer.
            if solution[house_index]["smokes"] == "Bluemaster" and solution[house_index]["drink"] != "Beer":
                return False

        def check_neighbors(house):
            for neighbor in [house - 1, house + 1]:
                if neighbor >= 0 and neighbor < 5:
                    if solution[neighbor] is None or used[house][solution[neighbor]]:
                        return False
            return True

        def check_constraints(house):
            if house == 1:
                # Constraint 9: The Norwegian lives in the first house.
                if solution[house]["nationality"] != "Norwegian":
                    return False
            elif house == 3:
                # Constraint 8: The man living in the center house drinks Milk.
                if solution[house]["drink"] != "Milk":
                    return False
            elif house == 4:
                # Constraint 10: The man who smokes Blends lives next to the one who keeps Cats.
                if solution[house - 2]["smokes"] != "Blends" or solution[house - 1]["pet"] != "Cat":
                    return False
                # Constraint 11: The man who keeps Horses lives next to the man who smokes Dunhill.
                if solution[house - 2]["pet"] != "Horse" or solution[house - 1]["smokes"] != "Dunhill":
                    return False
            elif house == 5:
                # Constraint 14: The Norwegian lives next to the Blue house.
                if solution[house - 1]["nationality"] != "Norwegian" or solution[house - 1]["color"] != "Blue":
                    return False
                # Constraint 15: The man who smokes Blends has a neighbor who drinks Water.
                if solution[house - 2]["smokes"] != "Blends" or solution[house - 1]["drink"] != "Water":
                    return False
            return True

        def assign_values(house):
            for nationality in nationalities:
                for color in colors:
                    for drink in drinks:
                        for smoke in smokes:
                            for pet in pets:
                                if check_constraints(house) and not used[house]:
                                    solution[house] = {k: v for k, v in zip([ "nationality", "color", "drink", "smokes", "pet" ], [ nationality, color, drink, smoke, pet ])}
                                    if house == 4 and (solution[house - 2]["smokes"] == "Blends" and solution[house - 1]["pet"] == "Cat"):
                                        return True
                                    used[house][solution[house]] = True
                                    if solve(house + 1):
                                        return True
                                    used[house].pop(solution[house])
            return False

        if assign_values(0):
            for house in range(5):
                print(f"House {house + 1}: Nationality: {solution[house]['nationality']}, Color: {solution[house]['color']}, Drink: {solution[house]['drink']}, Smokes: {solution[house]['smokes']}, Pet: {solution[house]['pet']}")
            print("Based on the constraints, the nationality of the person who keeps Fish as a pet is:", solution[0]["nationality"])

    solve(0)