def copy_list():
    list1 = [1, 2, 3], 
    list2 = []
    
    for item in list1:
        list2.append(item)
        
    return list2

def input_list():
    list = []

    while True:
        user_input = input("Enter an element to add: ")
        if user_input == "":
            break
        list.append(user_input)

    return list

# Test the functions
print("Copy List Function:")
list1_copy = copy_list()
print(list1_copy)

print("\nInput List Function:")
list2_input = input_list()
print(list2_input)