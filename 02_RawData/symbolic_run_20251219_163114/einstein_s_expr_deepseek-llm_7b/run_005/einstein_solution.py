def solve_puzzle():
    # Find all persons who keep pets and return their nationality
    pet_keepers = (exists(p) 
                   (and(is_a p "person") 
                    (keeps_pet p "Dog" "Bird" "Cat" "Horse" "Fish")) 
                   )
    
    # Filter the list of pet keepers to only include those who keep fish
    fish_keepers = filter(pet_keepers, (is_a p "person") 
                           (keeps_pet p "Fish"))
    
    # Get the nationality of the first person who keeps fish
    fish_nationality = get_first(fish_keepers, nationality_of)

    return fish_nationality