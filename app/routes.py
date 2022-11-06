from app import app, db
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, logout_user, current_user
from .models import Dataset, Daftar_slangwords, Daftar_stopwords, Users
from app.controllers.authcontroller import AuthController

@app.route('/beranda', methods=['GET'])
@app.route('/', methods=['GET'])
@login_required
def index():
    return render_template("/pages/index.html")

@app.route('/sign-up', methods=['GET', 'POST'])
def signUpRoute():
    if request.method == 'GET':
        return render_template("/auth/sign-up.html")
    elif request.method == 'POST':
        if AuthController(request.form).signUp():
            return redirect(url_for('index'))
        else:
            return render_template("/auth/sign-up.html")
        
@app.route('/sign-in', methods=['GET', 'POST'])
def signInRoute():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        else:
            return render_template("/auth/sign-in.html")
    elif request.method == 'POST':
        if AuthController(request.form).signIn():
            return redirect(url_for('index'))
        else:
            return render_template("/auth/sign-in.html")
            
@app.route('/sign-out', methods=['GET'])
def signOutRoute():
    AuthController().signOut()
    return redirect(url_for('signInRoute'))
    