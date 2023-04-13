def answer(s):
    # convert from string to list
    # s = s[1:-1]
    # s = s.split(",")

    import ast
    s = ast.literal_eval(s)
    print(s)

    lst = []
    for string in s:
        string = string.lower() 
        for char in [' ', ',', '.', ':', ';', "'", '"', '!', '?', '-']: 
            string = string.replace(char, '') 
        lst.append(string == string[::-1])
    return lst
    
def create_input():
    palindromes = [
        "A man, a plan, a canal, Panama!",
        "Was it a car or a cat I saw?",
        "Madam, in Eden, I'm Adam.",
        "Step on no pets.",
        "Eva, can I see bees in a cave?",
        "Mr. Owl ate my metal worm.",
        "Do geese see God?",
        "A Toyota's a Toyota.",
        "Never odd or even.",
        "Red roses run no risk, sir, on Nurse's order."
    ]

    not_palindromes = [
        "hello world",
        "palindrome",
        "ice cream is awesome",
        "not a palindrome",
        "this is not a palindrome",
        "racecars",
        "A man a plan a canal a Panama",
        "A Santa at NASO",
        "Madame",
        "Able was I ere I saw Elba!"
    ]

    # pick 5 palindromes and 5 not palindromes and randomise the order
    import random
    lst = []
    for _ in range(5):
        lst.append(random.choice(palindromes))
        lst.append(random.choice(not_palindromes))
    random.shuffle(lst)
    return lst