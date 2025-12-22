import string

def custom_sort(selkei):
    # sortu lo selkei sekundo lo clani be lo selkei 
    # i lo clani be lo selkei cu se sortu lo jmina
    return sorted([(c, a) for c, a in selkei], key=lambda x: (x[0].lower(), x[1]))
    
def main():
    string_list = ["apple", "fig", "banana", "cherry", "date"]
    
    # sortu lo navni lista sekundo lo re jalge 
    # i la'e di'u cu jalge:
    # 1. pa jalge: sortu lo selkei sekundo lo clani be lo selkei 
    #                i lo clani be lo selkei cu se sortu lo jmina
    # 2. re jalge: ji'a lo clani be lo selkei cu simsa lo sortu 
    #                i sortu lo selkei sekundo lo leksikografika (alfabetika) sortu
    
    sorted_list = custom_sort(string_list)
    
    print(sorted_list)

if __name__ == "__main__":
    main()