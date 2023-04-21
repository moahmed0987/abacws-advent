def answer(password_list):
    valid_passwords = 0
    for password in password_list:
        if len(password) < 16 or len(password) > 32:
            continue
        if not any(char.isupper() for char in password):
            continue
        if not any(char.islower() for char in password):
            continue
        if not any(char.isdigit() for char in password):
            continue
        if not any(char in "()!@#$%^&*-_+=|\\?/><.,;:'\"`~" for char in password):
            continue
        valid_passwords += 1
    return valid_passwords

def create_input():
    import random

    password_list = []
    for i in range(100000):
        password = ""
        length = random.randint(1, 48)
        while len(password) < length:
            if random.choice([True,False]):
                password += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            if random.choice([True,False]):
                password += random.choice("abcdefghijklmnopqrstuvwxyz")
            if random.choice([True,False]):
                password += random.choice("0123456789")
            if random.choice([True,False]):
                password += random.choice("()!@#$%^&*-_+=|\\?/><.,;:'\"`~")
        password_list.append(password)
    return password_list