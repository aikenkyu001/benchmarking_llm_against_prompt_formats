def solve_puzzle():
    nationalities = ["Brit", "Swede", "Dane", "Norwegian", "German"]
    colors = ["Red", "Green", "White", "Yellow", "Blue"]
    drinks = ["Tea", "Coffee", "Milk", "Beer", "Water"]
    smokes = ["Pall Mall", "Dunhill", "Blends", "Bluemaster", "Prince"]
    pets = ["Dog", "Bird", "Cat", "Horse", "Fish"]

    solution = {}
    used = {
        "nationality": set(),
        "color": set(),
        "drink": set(),
        "smokes": set(),
        "pet": set()
    }

    def solve(house_number):
        if house_number > 5:
            return True

        for nat in nationalities:
            if nat not in used["nationality"]:
                solution["house_" + str(house_number)] = nat
                used["nationality"].add(nat)

                for color in colors:
                    if color not in used["color"]:
                        solution["house_" + str(house_number)] = color
                        used["color"].add(color)

                        for drink in drinks:
                            if drink not in used["drink"]:
                                solution["house_" + str(house_number)] = drink
                                used["drink"].add(drink)

                                for smoke in smokes:
                                    if smoke not in used["smokes"]:
                                        solution["house_" + str(house_number)] = smoke
                                        used["smokes"].add(smoke)

                                        for pet in pets:
                                            if pet not in used["pet"]:
                                                solution["house_" + str(house_number)] = pet
                                                used["pet"].add(pet)

                                                if solve(house_number + 1):
                                                    return True

                                                # Backtrack
                                                used["pet"].remove(pet)

                                # Backtrack
                                used["smokes"].remove(smoke)

                        # Backtrack
                        used["drink"].remove(drink)

                # Backtrack
                used["color"].remove(color)

        return False

    if solve(1):
        print(solution["house_5"].get("nationality"))
    else:
        print("No solution found")