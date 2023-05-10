from advent_of_code import db
from advent_of_code.models import User, Puzzle, Attempt
from datetime import datetime, date, timedelta

db.drop_all()
db.create_all()

users = []
users.append(User(username='User1', email_address="user1@email.com", password="password", score=0))
users.append(User(username='User2', email_address="user2@email.com", password="password", score=10))
users.append(User(username='User3', email_address="user3@email.com", password="password", score=20))
users.append(User(username='User4', email_address="user4@email.com", password="password", score=30))
users.append(User(username='User5withaverylongname', email_address="user5withaverylongname@email.com", password="password", score=40000000000))

puzzles = []
puzzles.append(Puzzle(puzzle=
                      """Using the numbers on the grid, find the encrypted word by moving along the y-axis and down the x-axis. Determine the encrypted word for the following code: 3.4 5.3 4.5 2.5 1.1 2.4 5.1.""", 
                            type="logic", date=date.today(), answer="spyware", hint="""The code 2.1 corresponds to moving along the second row and down to the first column, which results in the letter "b"."""))
puzzles.append(Puzzle(puzzle=
                      "A hacker is using a messaging system that looks familiar... can you decrypt their message?\n01101000 01100001 01100011 01101011 01100101 01110010 01110011",
                            type="logic", date=date.today() + timedelta(days=1), answer="hackers", hint="https://en.wikipedia.org/wiki/ASCII#Printable_characters"))
puzzles.append(Puzzle(puzzle=
                      """Your password has been encrypted via Caesar cipher; you need to figure out the encrypted password to get past this stage. Your password is \"phishing\", find the encrypted word to solve this puzzle.""", 
                            type="logic", date=date.today() + timedelta(days=2), answer="tlmwlmrk", hint="""The outer ring of your Caesar Wheel represents the letters that make up your ACTUAL message ("plain text").  The inner ring of your Caesar Wheel shows you the letter you need to write in your CODED message ("cipher text").""",
                            image="q3.png"))
puzzles.append(Puzzle(puzzle=
                      "You are trying to access your computer, but your password has been locked. The following hint has been given to work out your password. \n1, VPN. \n2, firewall. \n4, encryption. \n2, authentication. \n1, spyware.",
                            type="logic", date=date.today() + timedelta(days=3), answer="virus", hint="The number corresponds to the placement of the letter in the password."))
puzzles.append(Puzzle(puzzle=
                      """You hear a strange beeping and note down the sequence, can you decrypt the message?\n
                      - .-. --- .--- .- -. """,
                            type="logic", date=date.today() + timedelta(days=4), answer="trojan", hint="https://en.wikipedia.org/wiki/Morse_code"))
puzzles.append(Puzzle(puzzle=
                      "A hacker is using some sort of hieroglyphics to encrypt a message... can you decrypt the message?",
                            type="logic", date=date.today() + timedelta(days=5), answer="security", hint="https://en.wikipedia.org/wiki/Pigpen_cipher", image="q6.png"))
puzzles.append(Puzzle(puzzle=
                      "The hacker has improved their encryption method, this time its much harder to crack. However, you recognise they appear to be using the affine cipher. Can you decrypt this final message?\nsaxc spisgcp",
                            type="logic", date=date.today() + timedelta(days=6), answer="code cracker", hint="https://en.wikipedia.org/wiki/Affine_cipher"))
puzzles.append(Puzzle(puzzle=
                      "Write a function that takes a list of integers and returns a new list that contains only the unique elements of the original list, in the same order.",
                              type="coding", date=date.today() + timedelta(days=7), answer="answer"))
puzzles.append(Puzzle(puzzle=
                      """Write a function that takes a list of strings and returns a list of True and False values indicating whether each string is a palindrome (i.e. reads the same forward and backward) \nThe function should ignore spaces, punctuation, and capitalisation. \nFor example, if the input is ["A man, a plan, a canal: Panama", "Not a palindrome."], the function should return [True, False].""",
                              type="coding", date=date.today() + timedelta(days=8), answer="answer"))
puzzles.append(Puzzle(puzzle=
                      """Given a list of passwords, determine how many passwords are valid according to this policy: \nPasswords must contain 1 uppercase letter, 1 lowercase letter, 1 number, 1 special character (()!@#$%^&*-_+=|\\?/><.,;:'\"`~), and between 16 and 32 characters.""",
                              type="coding", date=date.today() + timedelta(days=9), answer="answer"))
puzzles.append(Puzzle(puzzle=
                      """Write a program that evaluates arithmetic expressions with +, -, /, *, and parentheses according to the rules of operator precedence, where / and * have the same precedence and + and - have the same precedence. \nInput: a list of arithmetic expressions. \nOutput: the sum of the results of evaluating each expression rounding to 2 decimal places. \nFor example, if the input is ['3 * ( 2 + 6 ) / 52 - 9 - 64 / 7 / 9'], the output should be 23.00.""",
                              type="coding", date=date.today() + timedelta(days=10), answer="answer"))
puzzles.append(Puzzle(puzzle=
                      """Write a function that takes in a list of words and returns the longest compound word in the list, where a compound word is defined as a word made up of two other words from the list""",
                              type="coding", date=date.today() + timedelta(days=11), answer="answer"))
puzzles.append(Puzzle(puzzle=
                      """Write a function that takes a list of strings as input and returns the sum of the priority of the most common letter in each string. The priorities of the letters are determined by their position in the alphabet, with lowercase letters having priorities 1 through 26 and uppercase letters having priorities 27 through 52. For example, given the input ["ajdafasa", "amdmgmrmmf", "fjSotSwmSgd"], the function should return the sum of (1 * 4) + (13 * 5) + (45 * 3) = 4 + 65 + 135 = 204.""",
                              type="coding", date=date.today() + timedelta(days=12), answer="answer"))
puzzles.append(Puzzle(puzzle=
                      """Determine the bank notes and coins needed to make up a given amount of money using the denominations of £50, £20, £10, £5, £2, £1, 50p, 20p, 10p, 5p, 2p, and 1p. As an example, if the input amount is 133.48, the corresponding output should be [2, 1, 1, 0, 1, 1, 0, 2, 0, 1, 1, 1], which represents the number of each denomination required to form the given amount.""",
                              type="coding", date=date.today() + timedelta(days=13), answer="answer"))


attempts = []
attempts.append(Attempt(puzzle_id=1, user_id=1, attempt_data="Answer1", date=datetime.now(), correct=True, points_earned=10))
attempts.append(Attempt(puzzle_id=2, user_id=2, attempt_data="WrongAnswer", date=datetime.now(), correct=False, points_earned=0))
attempts.append(Attempt(puzzle_id=3, user_id=3, attempt_data="Answer3", date=datetime.now(), correct=True, points_earned=10))
attempts.append(Attempt(puzzle_id=4, user_id=4, attempt_data="WrongAnswer", date=datetime.now(), correct=False, points_earned=0))
attempts.append(Attempt(puzzle_id=5, user_id=5, attempt_data="WrongAnswer", date=datetime.now(), correct=False, points_earned=0))
attempts.append(Attempt(puzzle_id=5, user_id=5, attempt_data="WrongAnswer", date=datetime.now(), correct=False, points_earned=0))
attempts.append(Attempt(puzzle_id=5, user_id=5, attempt_data="CorrectAnswer", date=datetime.now(), correct=True, points_earned=8))

db.session.add_all(users)
db.session.add_all(puzzles)
db.session.add_all(attempts)
db.session.commit()