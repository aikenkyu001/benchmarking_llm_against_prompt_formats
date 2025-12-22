def solve_puzzle(task):
  """
  Solves the Einstein's Riddle logic puzzle using a custom token-based language.

  Args:
    task: A string representing the task, which is wrapped in `begin_DEFINE_TASK` and `end_DEFINE_TASK`.

  Returns:
    A string representing the final answer to the puzzle, or None if the task is invalid.
  """

  try:
    # Define the task
    task = task.strip()

    # Define the sets
    nationalities = ["Brit", "Swede"]
    drinks = ["Tea", "Coffee"]
    smokes = "Pall Mall"
    pets = "Bird"
    other_pets = "Horse"
    # Define the constraints
    # 1. The Brit drinks Tea.
    # 2. The Swede keeps Dogs as pets.
    # 3. The Dane drinks Tea.
    # 4. The Green house is on the left of the White house.
    # 5. The Green house's owner drinks Coffee.
    # 6. The person who smokes Pall Mall rears Birds.
    # 7. The owner of the Yellow house smokes Dunhill.
    # 8. The man living in the center house drinks Milk.
    # 9. The Norwegian lives next to the Blue house.
    # 10. The man who smokes Blends has a neighbor who drinks Water.

    # Solve the puzzle
    solution = [{} for _ in range(2)]
    used = {
      "nationality": set(),
      "drink": set()
    }
    def solve(house_index):
      if house_index == 2:
        # Constraint 1: The Brit drinks Tea.
        if not any(h.get("nationality") == "Brit" and h.get("drink") == "Tea" for h in solution):
          return False
        return True
      for nat in nationalities:
        if nat not in used["nationality"]:
          solution[house_index]["nationality"] = nat
          used["nationality"].add(nat)
      return False
    if solve(0):
      return "No solution found."
    elif solve(1):
      return "No solution found."
    else:
      return "The puzzle is unsolvable."

  except Exception as e:
    print(f"An error occurred: {e}")
    return None