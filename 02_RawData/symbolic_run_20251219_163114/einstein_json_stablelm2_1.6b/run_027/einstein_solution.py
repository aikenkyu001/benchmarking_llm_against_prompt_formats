def solve_puzzle():
    query = {
        "question": "Who keeps the Fish?",
         # Add any additional constraints or conditions here if needed.
        "return": "nationality",
        "of": {
            "pet": "Fish"
        }
    }

    for item in query["query"]["of"]:
        if item == "fish":
            return query["query"]["return"]

print(solve_puzzle())