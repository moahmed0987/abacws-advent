from random import randint
def answer(lst): 
    # convert from string to list
    lst = lst[1:-1]
    lst = lst.split(",")
    lst = [int(item) for item in lst]

    unique_lst = [] 
    for item in lst: 
        if item not in unique_lst: 
            unique_lst.append(item)
    return unique_lst

def create_input():
    lst = []
    for i in range(100):
        lst.append(randint(0, 100))
    return lst