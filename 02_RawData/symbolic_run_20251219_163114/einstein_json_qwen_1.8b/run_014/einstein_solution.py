def solve_puzzle(json_data):
    domains = json_data["domains"]
    
    for domain in domains:
        house_color = domain["color"]
        
        if house_color == "Red":
            nationality = domain["nationality"]
            
        else:
            nationality = "Unknown"
            
        print(nationality))