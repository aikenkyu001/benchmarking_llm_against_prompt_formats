def copy_list(source):
    """
    This function copies the elements from `source` to a new list without using any built-in functions or methods that directly copy lists.

    Parameters:
    source (list): The original list from which we want to copy elements.

    Returns:
    list: A new list containing the copied elements.
    """
    # Initialize an empty list to store the copied elements
    result = []

    # Iterate over each element in the source list
    for item in source:
        # Append each item to the result list
        result.append(item)

    return result

def input_list():
    """
    This function prompts the user to enter a list of elements and returns it as a list.

    Returns:
    list: The list of elements entered by the user.
    """
    # Prompt the user to enter a list of elements separated by spaces
    user_input = input("Enter a list of elements separated by spaces: ")

    # Split the input string into a list of strings
    elements = user_input.split()

    # Convert each string element to the appropriate type (int or float)
    result_list = [int(element) if element.isdigit() else float(element) for element in elements]

    return result_list

def main():
    """
    Main function to demonstrate the copying process.
    """
    # Get the list from the user
    input_list = input_list()

    # Copy the list using the custom copy_list function
    copied_list = copy_list(input_list)

    # Print the original and copied lists to verify the result
    print("Original List:", input_list)
    print("Copied List:", copied_list)

if __name__ == "__main__":
    main()