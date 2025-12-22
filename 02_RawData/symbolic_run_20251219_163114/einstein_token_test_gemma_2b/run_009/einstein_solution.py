def solve_puzzle():
    
    # All possible items for each category
    nationalities = ["Brit", "Swede", "Dane", "Norwegian", "German"]
    drinks = ["Tea", "Coffee", "Milk", "Beer", "Water"]
    smokes = ["Pall Mall", "Dunhill", "Blends", "Bluemaster", "Prince"]
    pets = ["Dog", "Bird", "Cat", "Horse", "Fish"]
    
    # This list will hold the solution, where each index is a house (0-indexed)
    solution = [{} for _ in range(2)]
    
    # Keep track of used items to ensure each is used only once
    used = {
        "nationality": set(),
        "drink": set(),
        "smokes": set(),
        "pets": set()
    }
    
    def solve(house_index):
        # Base case: if we have filled all houses, check if the solution is valid
        if house_index == 2:
            # Constraint 1: The Brit lives in the Red house.
            if not any(h.get("nationality") == "Brit" and h.get("pet") == "Fish" for h in solution):
                return False
            # Constraint 2: The Swede keeps Dogs as pets.
            if solution[1].get("nationality") != "Swede" or solution[1].get("pet") != "Dog":
                return False
            return True # All constraints met

        # Recursive step: Try to fill the current house (house_index)
        for nat in nationalities:
            if nat not in used["nationality"]:
                solution[house_index]["nationality"] = nat
                used["nationality"].add(nat)
                
                for drk in drinks:
                    if drk not in used["drink"]:
                        solution[house_index]["drink"] = drk
                        used["drink"].add(drk)
                        
                        # Move to the next house
                        if solve(house_index + 1):
                            return True
                        
                        # Backtrack
                        used["drink"].remove(drk)
                
                # Backtrack
                used["nationality"].remove(nat)
        
        return False

    if solve(0):
        # Find the answer to the query
        print(solution[0]["nationality"])