def solve_puzzle(puzzle):
    if puzzle == "German":
        return "Pinka"
    elif puzzle == "Sidbo":
        return "Ladru"
    else:
        return "Nu"

def solve_puzzle():
    print("Solving the puzzle...")
    puzzle = input("Enter the puzzle to be solved: ")
    puzzle = puzzle.lower()
    if puzzle == "German":
        return solve_puzzle(puzzle)
    elif puzzle == "Sidbo":
        return solve_puzzle(puzzle)
    else:
        print("Invalid puzzle.")