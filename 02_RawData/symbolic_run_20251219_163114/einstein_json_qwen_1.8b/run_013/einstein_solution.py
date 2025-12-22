def solve_puzzle(json_data):
    domains = json_data["domains"]
    
    # Check if the house number color is a specific color
    for house_color in domains:
        if house_color == "Red":
            return "nationality", "of" ["pet": "Fish"]]

# Define the JSON data
json_data = """
{
  "domains": [
    {
      "color": "Blue"
    }
  ]
}
"""

# Call the function and print the results
result = solve_puzzle(json_data)
print(f"The nationality of the fish owner is {result['of'][0]]}}")