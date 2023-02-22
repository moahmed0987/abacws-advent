from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from advent_of_code import db, login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True,nullable=False)
    email_address = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    score = db.Column(db.Integer, nullable=False, default=0)
    attempts = db.relationship("Attempt", backref="user")

    def __repr__(self):
        return f"User(id:'{self.id}', username:'{self.username}', email_address:'{self.email_address}', score:'{self.score}')"
    
    @property
    def password(self):
        raise AttributeError("Password is not readable.")
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Puzzle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    puzzle = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    answer = db.Column(db.String(1000), nullable=False)
    attempts = db.relationship("Attempt", backref="puzzle")

    def __repr__(self):
        return f"Puzzle(id:'{self.id}', puzzle:'{self.puzzle}', date:'{self.date}', answer:'{self.answer}')"

class Attempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    puzzle_id = db.Column(db.Integer, db.ForeignKey('puzzle.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    attempt_data = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Attempt(id:'{self.id}', puzzle_id:'{self.puzzle_id}', user_id:'{self.user_id}', attempt_data:'{self.attempt_data}', date:'{self.date}', score:'{self.score}')"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))