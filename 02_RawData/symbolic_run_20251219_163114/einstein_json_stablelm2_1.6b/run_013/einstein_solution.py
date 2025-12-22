def solve_puzzle():
    query = {
        "question": "Who keeps the Fish?",
         # Add any additional constraints or conditions here if needed.
        "return": "nationality",
        "of": {
            "pet": "Fish"
        }
    }

    def find_nationality(item):
        for category, items in query["domains"].items():
            if item[category] == query["of"][item["pet"]]:
                return query["nationality"][item["color"]]
        return None

    fish_owner = find_nationality(query["drink"][0])
    print(fish_owner)

solve_puzzle()