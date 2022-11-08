from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, template_folder="views", static_folder="static")
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:''@localhost/sentimen_afif'
app.config["SECRET_KEY"] = '8a4434eac74c483ee6902cf12ba089fb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_Manager = LoginManager(app)

from app import routes