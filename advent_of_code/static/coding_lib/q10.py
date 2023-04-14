def answer(password_list): 
    from ast import literal_eval
    password_list = literal_eval(password_list)

    valid_count = 0 
    for password in password_list:
        policy, password_str = password.split(": ")
        counts, letter = policy.split(" ") 
        min_count, max_count = [int(x) for x in counts.split("-")] 
        if min_count <= password_str.count(letter) <= max_count: 
            valid_count += 1 
    return valid_count

def create_input():
    inputs = [
        "1-6 b: bhfbbjxblj",
        "5-6 z: zzzzzxz",
        "7-12 h: hhhhhfhhhhhlhhhh",
        "7-10 g: gggtgggkgrgggggg",
        "5-7 r: rrjrdsrrrrm",
        "6-10 n: nndnnnnvnn",
        "9-10 t: ttjtttttmt",
        "6-10 h: hhhhhhhhhhhh",
        "6-7 w: wwwwwnfww",
        "3-5 g: gggnwgw",
        "4-5 l: llllll",
        "4-6 z: zzzqzqxzz",
        "1-4 s: sssgsbsskssssssssss",
        "8-10 l: llllllllgs",
        "9-12 d: ddddddddjdddd",
        "1-7 w: wwqzwkww",
        "2-4 l: llllll",
        "9-11 p: ppppppppppppppp",
        "4-5 p: mhppz",
        "12-13 z: zzzzzzzzzzzzz",
        "8-12 s: ssssssssssss",
        "6-11 h: hhhhhhhhhhfhh",
        "7-10 r: rrrrrrrrrrrrr",
        "5-6 v: vvvvkm",
        "6-12 g: gggggggggggggg",
        "5-6 r: wrrrxb",
        "3-6 f: fftffffff",
        "5-6 g: kgggng",
        "6-13 j: jjjjjjjjjjjjjjjj",
        "5-9 t: qtzttttht",
        "5-6 r: lrkfjrr",
        "5-7 d: ddddhdcd",
        "1-9 q: qqqqqqqqqqqqqqqq",
        "5-10 t: ttfttphtttttmthttp",
        "10-11 f: ffxfffdffff",
        "8-9 l: llllllllll",
        "3-7 b: bbbbbbm",
        "3-7 r: rrrrrrkrr",
        "2-8 b: cjbbkqbbqbq",
        "1-7 l: llllllnl",
        "3-4 l: lljj",
        "1-3 g: dgxg",
        "11-12 x: xxxxxxxxxxxd",
        "4-7 m: mmmgmmxmm",
        "2-6 t: tdttttpwttt",
        "6-11 s: qslmsnjvgfjsh",
        "2-6 m: mmmmmm",
        "3-4 t: ttth",
        "4-5 j: jzjjjjj",
        "4-6 z: zzkzdzcwpzh",
        "2-6 c: cccccccc",
        "2-3 p: pppppp",
        "2-9 d: ddddddddddd",
        "7-11 p: prldqxpvlpjpt",
        "3-5 n: snfxc",
        "1-3 z: zxbxnzmg",
        "7-10 w: kjnknwwvwwwwwwwwwwn",
        "5-6 v: vvrdvv",
        "3-5 k: kzkgk",
        "2-5 c: cccccccc",
        "10-14 g: ggwgfggjggggfhlg",
        "5-6 k: kkkkqhkkk",
        "5-11 f: fhfnfflfhjvwvfff",
        "4-7 d: mgdddddhkdqbddsddpm",
        "8-13 j: jjjjjjjjjjjjjjjjj",
        "6-8 h: hhhhhphphhhhhhhh"
    ]

    # return a random list of 10 inputs
    from random import sample
    return sample(inputs, 10)

s = answer(str(['5-6 v: vvvvkm', '6-7 w: wwwwwnfww', '5-6 k: kkkkqhkkk', '5-11 f: fhfnfflfhjvwvfff', '5-6 r: wrrrxb', '8-12 s: ssssssssssss', '7-11 p: prldqxpvlpjpt', '1-3 z: zxbxnzmg', '7-10 g: gggtgggkgrgggggg', '5-6 r: lrkfjrr']))
print(s)