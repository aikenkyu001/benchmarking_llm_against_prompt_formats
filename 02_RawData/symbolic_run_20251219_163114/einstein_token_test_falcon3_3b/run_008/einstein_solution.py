def solve_puzzle():
    # All possible items for each category
    nationalities = ["Brit", "Swede", "Dane", "Norwegian", "German"]
    colors = ["Red", "Green", "White", "Yellow", "Blue"]
    pets = ["Dog", "Bird", "Cat", "Horse", "Fish"]
    
    # This list will hold the solution, where each index is a house (0-indexed)
    solution = [{} for _ in range(5)]
    
    # Keep track of used items to ensure each is used only once
    used = {
        "nationality": set(),
        "color": set(),
        "pet": set()
    }

    def solve(house_index):
        if house_index == 5:
            return True # All constraints met

        for nat in nationalities:
            if nat not in used["nationality"]:
                solution[house_index]["nationality"] = nat
                used["nationality"].add(nat)
                
                for color in colors:
                    if color not in used["color"]:
                        solution[house_index]["color"] = color
                        used["color"].add(color)
                        
                        for pet in pets:
                            if pet not in used["pet"]:
                                solution[house_index]["pet"] = pet
                                used["pet"].add(pet)
                                
                                if solve(house_index + 1):
                                    return True
                            
                        used["color"].remove(color)
                    
                used["nationality"].remove(nat)
        
        return False

    if solve(0):
        for h in solution:
            if h.get("pet") == "Fish":
                print(h.get("nationality"))
                break