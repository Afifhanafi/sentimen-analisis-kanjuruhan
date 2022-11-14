from app import app, db
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, logout_user, current_user
from app.models import DatasetBefore, DatasetAfter
from app.controllers.authcontroller import AuthController
from app.controllers.slangwordcontroller import SlangwordController
from app.controllers.stopwordcontroller import StopwordController
from app.controllers.datacontroller import DataController
from app.controllers.labelcontroller import LabelController
from app.controllers.preprocessingcontroller import PreprocessingController
from app.controllers.testingcontroller import TestingController

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
    
    
@app.route('/kata-stop', methods=["GET", "POST"])
@login_required
def stopwordsRoute():
    if request.method == "GET":
        stopwords_data = StopwordController().retrieve()
        return render_template("/pages/stopwords.html", stopwords_data=stopwords_data)
    elif request.method == "POST" and request.files:
        StopwordController().importData(request.files["fileCSV"])
        return redirect(url_for('stopwordsRoute'))
    elif request.method == "POST" and request.form:
        StopwordController().create(request.form)
        return redirect(url_for('stopwordsRoute'))
    
@app.route('/kata-stop/ubah', methods=["GET", "POST"])
@login_required
def stopwordUpdateRoute():
    if request.method == "POST":
        StopwordController().update(request.form)
        return redirect(url_for('stopwordsRoute'))
    else:
        return redirect(url_for('stopwordsRoute'))
    
@app.route('/kata-stop/hapus', methods=["GET", "POST"])
@login_required
def stopwordDeleteRoute():
    if request.method == "POST":
        StopwordController().delete(request.form)
        return redirect(url_for('stopwordsRoute'))
    else:
        return redirect(url_for('stopwordsRoute'))

# Dataset Sebelum Tragedi Kanjuruhan
@app.route('/api/dataset-sebelum-tragedi-kanjuruhan', methods=["GET"])
def apiDatasetBeforeKanjuruhan():
    dataset = DataController().retrieveJSON(DatasetBefore)
    return dataset

@app.route('/dataset/dataset-sebelum-tragedi-kanjuruhan', methods=["GET", "POST"])
@login_required
def DatasetBeforeKanjuruhan():
    if request.method == "GET":
        return render_template("/pages/dataset_before.html")
    elif request.method == "POST" and request.files:
        DataController().importDataset(request.files["fileCSV"], DatasetBefore)
        return redirect(url_for('DatasetBeforeKanjuruhan'))

#Dataset Sesudah Kejadian Kanjuruhan
@app.route('/api/dataset-sesudah-tragedi-kanjuruhan', methods=["GET"])
def apiDatasetAfterKanjuruhan():
    dataset = DataController().retrieveJSON(DatasetAfter)
    return dataset

@app.route('/dataset/dataset-sesudah-tragedi-kanjuruhan', methods=["GET", "POST"])
@login_required
def DatasetAfterKanjuruhan():
    if request.method == "GET":
        return render_template("/pages/dataset_after.html")
    elif request.method == "POST" and request.files:
        DataController().importDataset(request.files["fileCSV"], DatasetAfter)
        return redirect(url_for('DatasetAfterKanjuruhan'))

#Pelabelan Sebelum Sebelum Tragedi Kanjuruhan
@app.route('/pelabelan/dataset-sebelum-tragedi-kanjuruhan', methods=["GET", "POST"])
@login_required
def labellingDatasetBefore():
    if request.method == 'POST':
        LabelController(request.form).updateDataset(DatasetBefore)
        return redirect(url_for('labellingDatasetBefore'))
    elif request.method == 'GET':
        return render_template('/pages/label_dataset_before.html')

@app.route('/pelabelan/dataset-sesudah-tragedi-kanjuruhan', methods=["GET", "POST"])
@login_required
def labellingDatasetAfter():
    if request.method == 'POST':
        LabelController(request.form).updateDataset(DatasetAfter)
        return redirect(url_for('labellingDatasetAfter'))
    elif request.method == 'GET':
        return render_template('/pages/label_dataset_after.html')

#Prapemrosesan Sebelum Tragedi Kanjuruhan
@app.route('/preprocessing/dataset-sebelum-tragedi-kanjuruhan', methods=["GET", "POST"])
@login_required
def preprocessingDatasetBefore():
    if request.method == 'POST':
        response = PreprocessingController().process(DatasetBefore)
        return response
    elif request.method == 'GET':
        jumlahDataset = DataController().retrieveData(DatasetBefore)
        return render_template('/pages/preprocessing_dataset_before.html', jumlahDataset=len(jumlahDataset))

@app.route('/preprocessing/dataset-sesudah-tragedi-kanjuruhan', methods=["GET", "POST"])
@login_required
def preprocessingDatasetAfter():
    if request.method == 'POST':
        response = PreprocessingController().process(DatasetAfter)
        return response
    elif request.method == 'GET':
        jumlahDataset = DataController().retrieveData(DatasetAfter)
        return render_template('/pages/preprocessing_dataset_after.html', jumlahDataset=len(jumlahDataset))

#Pengujian Sebelum Tragedi Kanjuruhan
@app.route('/pengujian/dataset-sebelum-tragedi-kanjuruhan', methods=["GET", "POST"])
@login_required
def testingDatasetBefore():
    if request.method == 'POST':
        response = TestingController(DatasetBefore).processTest(request.form)
        return response
    elif request.method == 'GET':
        totalSplit = DataController().retrieveCountData(DatasetBefore)
        return render_template('/pages/testing_dataset_before.html', totalSplit = int(totalSplit))

@app.route('/pengujian/dataset-sesudah-tragedi-kanjuruhan', methods=["GET", "POST"])
@login_required
def testingDatasetAfter():
    if request.method == 'POST':
        response = TestingController(DatasetAfter).processTest(request.form)
        return response
    elif request.method == 'GET':
        totalSplit = DataController().retrieveCountData(DatasetAfter)
        return render_template('/pages/testing_dataset_after.html', totalSplit = int(totalSplit))

@app.errorhandler(401)
def unauthorized(error):
    return redirect(url_for('signInRoute'))

@app.errorhandler(404)
def pageNotFound(error):
    return render_template("/pages/404.html")