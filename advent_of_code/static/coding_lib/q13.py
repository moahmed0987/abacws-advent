def create_input(num_inputs=10):
    from random import choice, randint
    from string import ascii_letters as chars
    inputs = []
    for i in range(num_inputs):
        common_char = choice(chars)
        input = []
        for j in range(randint(8, 16)):
            input.append(choice(chars))
        for j in range(randint(4, 8)):
            input.insert(randint(0, len(input)), common_char)
        inputs.append("".join(input))
    return inputs 
    
def answer(inputs):
    from ast import literal_eval
    inputs = literal_eval(inputs)

    from string import ascii_letters as chars
    from collections import Counter
    sum = 0
    for input in inputs:
        counter = Counter(input)
        most_common = counter.most_common(1)[0][0]
        print(most_common)
        sum += (chars.index(most_common) + 1) * counter[most_common]
    return sum