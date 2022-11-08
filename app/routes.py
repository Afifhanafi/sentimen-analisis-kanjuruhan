from app import app, db
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, logout_user, current_user
from app.controllers.authcontroller import AuthController
from app.controllers.slangwordcontroller import SlangwordController
from app.controllers.datacontroller import DataController

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

@app.route('/kata-slang', methods=["GET", "POST"])
@login_required
def slangwordsRoute():
    if request.method == "GET":
        slangwords_data = SlangwordController().retrieve()
        return render_template("/pages/slangwords.html", slangwords_data=slangwords_data)
    elif request.method == "POST" and request.files:
        SlangwordController().importData(request.files["fileCSV"])
        return redirect(url_for('slangwordsRoute'))
    elif request.method == "POST" and request.form:
        SlangwordController().create(request.form)
        return redirect(url_for('slangwordsRoute'))

@app.route('/kata-slang/ubah', methods=["GET", "POST"])
@login_required
def slangwordUpdateRoute():
    if request.method == "POST":
        SlangwordController().update(request.form)
        return redirect(url_for('slangwordsRoute'))
    else:
        return redirect(url_for('slangwordsRoute'))

@app.route('/kata-slang/hapus', methods=["GET", "POST"])
@login_required
def slangwordDeleteRoute():
    if request.method == "POST":
        SlangwordController().delete(request.form)
        return redirect(url_for('slangwordsRoute'))
    else:
        return redirect(url_for('slangwordsRoute'))
    
@app.route('/api/dataset-sebelum-tragedi-kanjuruhan', methods=["GET"])
@login_required
def apiDatasetBeforeKanjuruhan():
    dataset = DataController().retrieveBefore()
    return dataset

@app.route('/dataset/dataset-sebelum-tragedi-kanjuruhan', methods=["GET", "POST"])
@login_required
def DatasetBeforeKanjuruhan():
    if request.method == "GET":
        return render_template("/pages/dataset_before.html")
    elif request.method == "POST" and request.files:
        DataController().importDatasetBefore(request.files["fileCSV"])
        return redirect(url_for('DatasetBeforeKanjuruhan'))
    
@app.errorhandler(401)
def unauthorized(error):
    return redirect(url_for('signInRoute'))

@app.errorhandler(404)
def pageNotFound(error):
    return render_template("/pages/404.html")