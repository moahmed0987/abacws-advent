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
                      """Using the numbers on the grid, find the encrypted word by moving along the y-axis and down the x-axis. For example, the code 2.1 corresponds to moving along the second row and down to the first column, which results in the letter "b". Determine the encrypted word for the following code: 3.4 5.3 4.5 2.5 1.1 2.4 5.1.""", 
                       date=date.today(), answer="spyware"))
puzzles.append(Puzzle(puzzle="Puzzle1", date=date.today() + timedelta(days=1), answer="Answer1"))
puzzles.append(Puzzle(puzzle="Puzzle2", date=date.today() + timedelta(days=2), answer="Answer2"))
puzzles.append(Puzzle(puzzle="Puzzle3", date=date.today() + timedelta(days=3), answer="Answer3"))
puzzles.append(Puzzle(puzzle="Puzzle4", date=date.today() + timedelta(days=4), answer="Answer4"))
puzzles.append(Puzzle(puzzle="Puzzle5", date=date.today() + timedelta(days=5), answer="Answer5"))

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