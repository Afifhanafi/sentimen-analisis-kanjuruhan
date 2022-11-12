from app import db, login_Manager
from flask_login import UserMixin

class DatasetBefore(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.String(100))
    username = db.Column(db.String(100))
    raw_tweets = db.Column(db.Text)
    clean_tweets = db.Column(db.Text)
    label = db.Column(db.String(10))
    
    def __repr__(self):
        return '<Dataset Before {}>'.format(self.raw_tweets)

class DatasetAfter(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.String(100))
    username = db.Column(db.String(100))
    raw_tweets = db.Column(db.Text)
    clean_tweets = db.Column(db.Text)
    label = db.Column(db.String(10))
    
    def __repr__(self):
        return '<Dataset After {}>'.format(self.raw_tweets)
    
class Daftar_slangwords(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    kata_slang = db.Column(db.String(100))
    kata_baku = db.Column(db.String(100))

    def __repr__(self):
        return '<Kata Slang {}>'.format(self.kata_slang)

class Daftar_stopwords(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    stopwords = db.Column(db.String(100))
    
    def __repr__(self):
        return '<Kata Stop {}>'.format(self.stopwords)
    
class Users(db.Model, UserMixin):
    id = db.Column(db.SmallInteger, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return '<Username {}>'.format(self.username)
    
@login_Manager.user_loader
def loadUser(user_id):
    return Users.query.filter_by(id = int(user_id)).first()