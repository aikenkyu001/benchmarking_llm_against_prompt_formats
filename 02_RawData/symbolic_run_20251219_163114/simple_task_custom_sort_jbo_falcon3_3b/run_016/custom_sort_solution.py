def custom_sort(string_list):
    # Step 1: Sort by length of words (pa jalge)
    string_list.sort(key=lambda x: len(x))
    
    # Step 2: Sort by alphabetical order (re jalge)
    string_list.sort()

def main():
    # Initial list
    initial_list = ["apple", "fig", "banana", "cherry", "date"]
    
    # Apply custom sort
    custom_sort(initial_list)
    
    # Print the sorted list
    print("Sorted List:", initial_list)

if __name__ == "__main__":
    main()