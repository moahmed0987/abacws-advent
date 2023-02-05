from advent_of_code import app

@app.route('/')
def home():
    return 'Home Page'