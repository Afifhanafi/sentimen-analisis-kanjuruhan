from app import app
from flask import render_template

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/sign-up', methods=['GET'])
def signUp():
    return render_template("/auth/sign-up.html")

@app.route('/sign-in', methods=['GET', 'POST'])
def signIn():
    return render_template("/auth/sign-in.html")

    