from app import app, db
from flask import render_template, request, session, flash, redirect, url_for
from flask_login import login_required
from .models import Dataset, Daftar_slangwords, Daftar_stopwords, Users

@app.route('/', methods=['GET'])
# @login_required
def index():
    return render_template("index.html")

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
        
        return redirect(url_for('index'))
    return render_template("/auth/sign-up.html")

@app.route('/sign-in', methods=['GET', 'POST'])
def signIn():
    return render_template("/auth/sign-in.html")

    