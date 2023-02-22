from datetime import date, datetime, timedelta

from flask import flash, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required, login_user, logout_user

from advent_of_code import app, db, login_manager
from advent_of_code.forms import LoginForm, PuzzleForm, RegistrationForm
from advent_of_code.models import Puzzle, User, Attempt

login_manager.login_view = "login"

@app.route('/')
def home():
    return render_template("index.html", title="Advent of Code")
    
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username_new.data, email_address=form.email_address_new.data, password=form.password_new.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user, remember=form.remember_me.data, duration=timedelta(days=7))

        if "redirect" in session:
            direction = session["redirect"]
            del session["redirect"]
            return redirect(direction)

        return redirect(url_for("home"))

    return render_template("login.html", title="Login", form=form)

@app.route("/puzzle/<puzzle_date>", methods=["GET", "POST"])
@login_required
def puzzle(puzzle_date):
    # if user is not logged in, redirect to login page
    if current_user.is_authenticated == False:
        session["redirect"] = url_for("puzzle", puzzle_date=puzzle_date)
        return redirect(url_for("login"))

    # if puzzle_date is "today", redirect to today's puzzle
    if puzzle_date == "today":
        puzzle_date = date.today().strftime("%Y-%m-%d")
        return redirect(url_for("puzzle", puzzle_date=puzzle_date))

    # if puzzle_date is invalid, redirect to error page
    try:
        puzzle_date = datetime.fromisoformat(puzzle_date)
    except ValueError:
        return "404 - Invalid date", 404
        # TODO: add error handling page

    # get puzzle for puzzle_date
    puzzle = Puzzle.query.filter_by(date=puzzle_date).first()
    if puzzle is None:
        return "404 - Puzzle not found", 404
        # TODO: add error handling page
    
    title_date = puzzle_date.strftime("%Y-%m-%d")

    # form for submitting answer
    form = PuzzleForm()
    if form.validate_on_submit():
        # create attempt. if answer is correct, update user score. if not, update attempt count. 
        if form.answer.data == puzzle.answer:
            attempt = Attempt(user_id=current_user.id, puzzle_id=puzzle.id, attempt_data=form.answer.data, date=datetime.now(), correct=True)
            current_user.score += 10
            # TODO: show success message
        else:
            attempt = Attempt(user_id=current_user.id, puzzle_id=puzzle.id, attempt_data=form.answer.data, date=datetime.now(), correct=False)
            # TODO: show failure message
        db.session.add(attempt)
        db.session.commit()
        

    return render_template("puzzle.html", title=title_date, form=form, puzzle=puzzle)

@app.route("/leaderboard")
def leaderboard():
    # get top 100 users ordered by score
    users = User.query.order_by(User.score.desc()).limit(100).all()
    return render_template("leaderboard.html", title="Leaderboard", users=users)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))