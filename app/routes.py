from app import app
from flask import render_template

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("/auth/login.html")