def solve_puzzle(puzzle):
    domains = puzzle["domains"]
    constraints = puzzle["constraints"]

    if len(domains) == 0 or len(constraints) == 0:
        return "No puzzles found"

    for domain in domains:
        if domain not in puzzle["types"]:
            return f"Domain {domain} is missing from the puzzle"

        if puzzle["type"] == "association":
            if puzzle["type"] == "is_left_of":
                return f"The fish owner is left-handed, but the house number is right-handed."
            elif puzzle["type"] == "is_neighbor_of":
                return f"The fish owner lives next to a house with a different color of paint."
        else:
            if puzzle["type"] == "positional":
                return f"The fish owner is left-handed, but the dog is right-handed."

    return f"All puzzles found in the JSON file are correct. The Fish is {puzzle['type']} and the Dog is {puzzle['type']}."