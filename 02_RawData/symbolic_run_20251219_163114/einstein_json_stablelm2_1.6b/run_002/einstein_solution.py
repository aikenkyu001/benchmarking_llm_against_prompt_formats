def solve_puzzle():
    # Parse the JSON data
    data = json.loads("""
    {
        "domains": [
            {"house_number": [1, 2, 3, 4, 5], "color": ["Red", "Green", "White", "Yellow", "Blue"], "nationality": ["Brit", "Swede", "Dane", "Norwegian", "German"], "drink": ["Tea", "Coffee", "Milk", "Beer", "Water"], "smoke": ["Pall Mall", "Dunhill", "Blends", "Bluemaster", "Prince"], "pet": ["Dog", "Bird", "Cat", "Horse", "Fish"]}, 
            ... # more domains
        ], 
        "constraints": [
            ...
        ], 
        "query": {
            "question": "Who keeps the Fish?",
            "return": "nationality",
            "of": {  "pet": "Fish" }  
        }
    }
    """)

    # Extract the information from the query
    fish_owner = data["query"]["of"]

    # Find the nationality of the fish owner based on the given information
    for domain in data["domains"]:
        if domain["pet"] == "Fish":
            return domain["nationality"][fish_owner.index(fish_owner) % len(domain["nationality"])]

    print("Unknown")