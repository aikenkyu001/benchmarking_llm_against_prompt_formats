def solve_puzzle(json_data):
    domains = json_data["domains"]
    
    for domain in domains:
        house_color = domain["color"]
        
        if house_color == "Red":
            nationality = domain["nationality"]
            
        else:
            nationality = "Unknown"
            
        print(f"Question: Who keeps the {house_color} fish? Answer: {nationality}}")  # Output: