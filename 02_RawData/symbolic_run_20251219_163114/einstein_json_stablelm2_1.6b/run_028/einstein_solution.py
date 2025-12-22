def solve_puzzle():
    query = {
        "question": "Who keeps the Fish?",
         # Add any additional constraints or conditions here if needed.
        "return": "nationality",
        "of": {
            "pet": "Fish"
        }
    }

    data = {
        "domains": {
            "house_number": [1, 2, 3, 4, 5],
            "color": ["Red", "Green", "White", "Yellow", "Blue"],
            "nationality": ["Brit", "Swede", "Dane", "Norwegian", "German"],
            "drink": ["Tea", "Coffee", "Milk", "Beer", "Water"], 
            "smoke": ["Pall Mall", "Dunhill", "Blends", "Bluemaster", "Prince"], 
            "pet": ["Dog", "Bird", "Cat", "Horse", "Fish"]
        },
        "constraints": [
            {
                "type": "association",
                "subject": {"nationality": "Brit"},
                "object": {"color": "Red"}
            },
            # Add more constraints as needed.
        ],
        "query": query
    }

    for category, items in data["domains"].items():
        for item in items:
            if query["of"][item] == query["subject"]:
                answer = item
                break

    print(answer)