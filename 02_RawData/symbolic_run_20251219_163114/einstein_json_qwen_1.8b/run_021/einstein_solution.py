def solve_puzzle(json_data):
    domains = json_data["domains"]
    
    # Check if the house number color is a specific color
    for house_color in domains:
        if house_color == "Red":
            return "nationality", "of" ["pet": "Fish"]  # Change pet to desired color

    # Return the nationality of the fish owner based on the house number color
    return "nationality", domains[0]["color"]]

json_data = '{"domains":[{"house_number_color":"Red"},{"house_number_color":"Blue"},{"house_number_color":"Green"}],"return":{"nationality":"Norwegian"}}}'  # Replace 'red' with desired house number color

print(solve_puzzle(json_data))))