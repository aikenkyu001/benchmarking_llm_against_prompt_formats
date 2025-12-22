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

            # Add more domains if needed.
        },

        "constraints": [
            {
                "type": "association",
                "subject": {"nationality": "Brit"},
                "object": {"color": "Red"}
            },
            # Add more constraints here if needed.
        ],

        "query": query
    }

    for domain, items in data["domains"].items():
        for item in items:
            if item[domain] not in [x['nationality'] for x in data["nationality"]]:
                break

    print(data["nationality"][data["query"]["of"] - 1])