def solve_puzzle():
    # Define the sets and constraints
    house_numbers = [1, 2, 3, 4, 5]
    colors = ["Red", "Green", "White", "Yellow", "Blue"]
    nationalities = ["Brit", "Swede", "Dane", "Norwegian", "German"]
    drinks = ["Tea", "Coffee", "Milk", "Beer", "Water"]
    smokes = ["Pall Mall", "Dunhill", "Blends", "Bluemaster", "Prince"]
    pets = ["Dog", "Bird", "Cat", "Horse", "Fish"]
    smokes_adj = {"Pall Mall": "Dunhill", "Dunhill": "Blends", "Bluemaster": "Prince"}
    
    # Define the backtracking function
    def backtrack(house_index, used):
        if house_index == 2:
            # Constraint 1: The Brit drinks Tea.
            if not any(nat in used["nationality"] for nat in ["Brit", "Swede"]) or \
                not any(drink in used["drink"] for drink in ["Tea"]):
                return False
            # Constraint 2: The Swede lives in house 2.
            if solution[house_index - 1].get("nationality") != "Swede":
                return False
        for nat in nationalities:
            if nat not in used["nationality"]:
                solution[house_index]["nationality"] = nat
                used["nationality"].add(nat)
                for drk in drinks:
                    if drk not in used["drink"]:
                        solution[house_index]["drink"] = drk
                        used["drink"].add(drk)
                        if backtrack(house_index + 1, used):
                            return True
                used["nationality"].remove(nat)
        return False

    # Define the query and solve function
    def query():
        print("Based on the constraints, determine the nationality of the person who keeps Fish as a pet.")
        
        for i in range(len(pets)):
            if pets[i] not in used["pet"]:
                solution[0]["pet"] = pets[i]
                used["pet"].add(pets[i])
                if backtrack(0, used):
                    return
                used["pet"].remove(pets[i])

    # Solve the puzzle
    solution = [[] for _ in range(len(house_numbers))]
    used = {nationality: set() for nationality in nationalities}
    
    if not backtrack(0, used):
        print("No solution found.")
        return

    query()
    print("The answer is:", solution[0]["nationality"])

solve_puzzle()