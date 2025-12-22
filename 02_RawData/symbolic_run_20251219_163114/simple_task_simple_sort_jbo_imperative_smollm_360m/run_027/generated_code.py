import random

def simple_sort(lst):
    lst.sort()
    return lst

def number_list(lst):
    return sorted([random.randint(-10, 10) for _ in range(len(lst))])

def funkci'o_cmene(lst):
    return "Simple Sort"

def simple_sort_with_counters(lst):
    lst.sort()
    counter = 0
    while len(lst) > 1:
        if counter % 2 == 0:
            lst.sort()
        else:
            lst.sort(reverse=True)
        counter += 1
    return lst