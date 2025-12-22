def solve_puzzle():
    house_numbers = [1, 2, 3, 4, 5]
    colors = ["Red", "Green", "White", "Yellow", "Blue"]
    nationalities = ["Brit", "Swede", "Dane", "Norwegian", "German"]
    drinks = ["Tea", "Coffee", "Milk", "Beer", "Water"]
    smokes = ["Pall Mall", "Dunhill", "Blends", "Bluemaster", "Prince"]
    pets = ["Dog", "Bird", "Cat", "Horse", "Fish"]

    used = {
        "nationality": set(),
        "drink": set(),
        "smoke": set(),
        "pet": set()
    }

    def solve(house_index):
        if house_index == 5:
            return True

        for nat in nationalities:
            if nat not in used["nationality"]:
                used["nationality"].add(nat)

                for drk in drinks:
                    if drk not in used["drink"]:
                        used["drink"].add(drk)

                        for smk in smokes:
                            if smk not in used["smoke"]:
                                used["smoke"].add(smk)

                                for pet in pets:
                                    if pet not in used["pet"]:
                                        used["pet"].add(pet)

                                        # Move to the next house
                                        if solve(house_index + 1):
                                            return True

                                        # Backtrack
                                        used["pet"].remove(pet)
                                        
                                # Backtrack
                                used["smoke"].remove(smk)
                                
                            # Backtrack
                            used["drink"].remove(drk)
                            
                        # Backtrack
                        used["nationality"].remove(nat)

        return False

    if solve(0):
        for h in range(5):
            if colors[h] == "Green":
                print("The person who keeps Fish as a pet is the " + nationalities[house_numbers.index(h+1)])