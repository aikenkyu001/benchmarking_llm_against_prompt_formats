def solve_puzzle():
    assert(exists((p) and (is_a(p) and (keeps_pet(p) == "Fish")))(and (nationality_of p == "Norwegian") and (has_neighbor(house_number, 1) == True)))
    
    query = "Who keeps the Fish?"
    result = find((p) and (is_a(p) and (keeps_pet(p) == "Fish")))(nationality_of p)
    
    print(result)

solve_puzzle()