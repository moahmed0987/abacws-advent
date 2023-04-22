def answer(words):
    from ast import literal_eval
    words = literal_eval(words)

    word_set = set(words) 
    longest_compound_word = ""
    for word in words:
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in word_set and suffix in word_set:
                if len(word) > len(longest_compound_word):
                    longest_compound_word = word
                break  
    return longest_compound_word

def create_input():
    from random import choice, randint, shuffle
    from os.path import join as os_path_join, dirname as os_path_dirname
    with open(os_path_join(os_path_dirname(__file__), "words_alpha.txt")) as f:
        word_list = f.read().splitlines()

    input = []
    compound_words = []
    for i in range(randint(900, 950)):
        input.append(choice(word_list))
    for i in range((1000 - len(input)) // 2):
        word1 = choice(input)
        word2 = choice(input)
        compound_word = word1 + word2
        if len(compound_word) <= 18:
            compound_words.append(compound_word)
    input.extend(compound_words)
    while len(input) < 1000:
        word = choice(word_list)
        if len(word) > len(max(compound_words, key=len)):
            input.append(word)
    shuffle(input)
    return input