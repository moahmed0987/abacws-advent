from datetime import timedelta
from flask import redirect, render_template, request, session, url_for
from flask_login import current_user, login_required, login_user, logout_user

from advent_of_code import app, db, login_manager
from advent_of_code.forms import LoginForm, RegistrationForm
from advent_of_code.models import User
login_manager.login_view = "login"

@app.route('/')
def home():
    return render_template("index.html", title="Home")
    
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
        login_user(user, remember=form.remember_me.data,duration=timedelta(days=7))

        if "redirect" in session:
            return redirect(session["redirect"])

        return redirect(url_for("home"))

    return render_template("login.html", title="Login", form=form)

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