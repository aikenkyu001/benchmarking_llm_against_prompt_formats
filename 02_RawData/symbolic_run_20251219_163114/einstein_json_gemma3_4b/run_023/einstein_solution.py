def solve_puzzle():
    fish_owners = {}
    for constraint in constraints:
        if constraint["type"] == "association" and constraint["object"]["pet"] == "Fish":
            fish_owners[constraint["subject"]["nationality"]] = constraint["subject"]["nationality"]
    print(fish_owners["German"])