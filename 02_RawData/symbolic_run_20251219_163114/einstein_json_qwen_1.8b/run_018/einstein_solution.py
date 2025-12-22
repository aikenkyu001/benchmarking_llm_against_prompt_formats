def solve_puzzle(json_data):
    domains = json_data["domains"]
    
    # Check if the house number is present in all domains

    for domain in domains:
        house_number = domain.get("house_number")
        
        if house_number not in [1, 2, 3, 4, 5], 1]:
            return "nationality"
    
    # Check if the color of the fish is present in all domains

    colors = json_data["colors"]
    
    for domain in domains:
        color = domain.get("color")
        
        if color not in [1, 2, 3, 4, 5], 1]:
            return "color"
    
    # Check if the smoke of the fish is present in all domains

    smokes = json_data["smokes"]
    
    for domain in domains:
        smoke = domain.get("smoke")
        
        if smoke not in [1, 2, 3, 4, 5], 1]:
            return "smoke"
    
    # Check if the nationality of the fish owner is present in all domains

    nationalities = json_data["nationalities"]
    
    for domain in domains:
        nationality = domain.get("nationality")
        
        if nationality not in [1, 2, 3, 4, 5], 1]:
            return "nationality"
    
    # Check if the query is correct

    if json_data["query"] != "Who keeps the Fish?" and json_data["query"] != "Norwegian fish owner" and json_data["query"] != "Blue smoke":
        return "query"

# Return the final result
return nationalities