from app import app, db
from flask import render_template, request, session, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from .models import Dataset, Daftar_slangwords, Daftar_stopwords, Users

@app.route('/', methods=['GET'])
@login_required
def index():
    return render_template("index.html", username=current_user)

@app.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        user = Users.query.filter_by(username = request.form['username']).first()
        if user:
            flash(f"Username sudah terdaftar", "danger")
            return render_template("/auth/sign-up.html")
        
        new_user = Users(
            username = request.form['username'],
            password = request.form['password']
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        session['id'] = new_user.id
        session['username'] = new_user.username
        login_user(new_user)
        
        return redirect(url_for('index'))
    return render_template("/auth/sign-up.html")

@app.route('/sign-in', methods=['GET', 'POST'])
def signIn():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    elif request.method == 'POST':
        user = Users.query.filter_by(username = request.form['username']).first()
        if not user:
            flash(f"Username tidak terdaftar", "danger")
            return render_template("/auth/sign-in.html")
        elif request.form['password'] != user.password:
            flash(f"Password anda salah", "danger")
            return render_template("/auth/sign-in.html")
        else:
            # session['id'] = user.id
            # session['username'] = user.username
            
            login_user(user)
        
        return redirect(url_for('index'))
    return render_template("/auth/sign-in.html")

@app.route('/sign-out')
def signOut():
    # session.pop('id', None)
    # session.pop('username', None)
    
    logout_user()
    
    flash(f"Anda sudah sign out", "warning")
    return redirect(url_for('signIn'))
    