def answer(list_amounts):
    from ast import literal_eval
    list_amounts = literal_eval(list_amounts)
    from decimal import Decimal
    list_amounts = [Decimal(str(amount)) for amount in list_amounts] 

    denominations = [50, 20, 10, 5, 2, 1, 0.50, 0.2, 0.1, 0.05, 0.02, 0.01] 
    denominations = [Decimal(str(denomination)) for denomination in denominations]
    result = []
    for amount in list_amounts:
        amount = Decimal(amount)
        notes = []
        for d in denominations:
            count = amount // d
            amount %= d
            notes.append(count)
        result.append(notes)
    # convert to int
    result = [[int(note) for note in notes] for notes in result]
    return result

def create_input():
    import random
    list_amounts = []
    for _ in range(100):
        amount = random.randint(1, 10000)
        amount = amount / 100
        list_amounts.append(amount)
    print(list_amounts)
    return list_amounts

s = create_input()
print(answer(str(s)))