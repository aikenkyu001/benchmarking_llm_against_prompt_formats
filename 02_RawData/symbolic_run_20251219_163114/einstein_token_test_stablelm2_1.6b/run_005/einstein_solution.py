def solve_puzzle():
    # Define sets for each category
    nationalities = ["Brit", "Swede"]
    drinks = ["Tea", "Coffee"]
    colors = ["Red", "Green", "White", "Yellow", "Blue"]
    smokes = ["Pall Mall", "Dunhill", "Blends", "Bluemaster", "Prince"]
    pets = ["Dog", "Bird", "Cat", "Horse", "Fish"]
    
    # Define the house numbers and their corresponding nationalities
    house_numbers = [1, 2, 3, 4, 5]
    house_nationalities = [nationalities[i] for i in house_numbers]
    
    # Define the drinks and their corresponding pets
    drink_pets = {smokes[i]: pets[i] for i in range(len(smokes))}
    
    # Define the query
  # "Who drinks Coffee?"
    query = "Based on the constraints, determine the nationality of the person who keeps Fish as a pet."

    # Define the solution
    solution = {}
    
    # Define the used items dictionary
    used_items = {
        "nationality": set(),
        "drink": set()
    }
    
    # Define the recursive function to solve the puzzle
    def solve(house_index):
        # Base case: if we have filled all houses, check if the solution is valid
        if house_index == 5:
            # Constraint 1: The Brit drinks Tea.
            if not any(nationality for nationality in house_nationalities) or \
                not any(drink for drink_pet in drink_pets.values()) for nationalities, drink_pet in zip(house_nationalities, drink_pets.values())):
                return True
        # Recursive step: Try to fill the current house (house_index)
        for nationality in house_nationalities:
            if nationality not in used_items["nationality"] or \
                not any(drink for drink_pet in drink_pets.values()) for drink_pet, _ in zip(smokes, drink_pets.values())):
                solution[house_index] = nationality
                used_items["nationality"].add(nationality)
                used_items["drink"].add(drink_pet)
                if solve(house_index + 1):
                    return True
                used_items["drink"].remove(drink_pet)
        return False

    # Solve the puzzle
    if solve(0):
        # Find the answer to the query
        for house in solution:
            if house.get("drink") == "Coffee":
                print(house.get("nationality"))
                return