from app import db
from flask import request, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from app.models import Users

class AuthController():
    def __init__(self, *args):
        if args:
            self.username = args[0]["username"]
            self.password = args[0]["password"]
    
    def signIn(self):
        user = Users.query.filter_by(username = self.username).first()
        if not user:
            flash(f"Username tidak terdaftar", "danger")
            return False
        elif self.password != user.password:
            flash(f"Password anda salah", "danger")
            return False
        else:
            login_user(user)
            return True
    
    def signUp(self):
        user = Users.query.filter_by(username = self.username).first()
        if user:
            flash(f"Username sudah terdaftar", "danger")
            return False
        else:
            new_user = Users(
                username = self.username,
                password = self.password
            )
            
            db.session.add(new_user)
            db.session.commit()
            
            login_user(new_user)
            return True
    
    def signOut(self):
        logout_user()
        flash(f"Anda telah keluar", "warning")
        return