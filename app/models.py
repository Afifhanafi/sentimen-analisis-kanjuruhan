from app import db

class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.String(100))
    username = db.Column(db.String(100))
    raw_tweets = db.Column(db.Text)
    clean_tweets = db.Column(db.Text)
    label = db.Column(db.String(10))
     
    
class Daftar_slangwords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kata_slang = db.Column(db.String(100))
    kata_baku = db.Column(db.String(100))


class Daftar_stopwords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stopwords = db.Column(db.String(100))