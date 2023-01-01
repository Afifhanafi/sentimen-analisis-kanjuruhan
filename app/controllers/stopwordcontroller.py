from app import db
from flask import flash
from app.models import Daftar_stopwords
import pandas as pd
class StopwordController:
    def importData(self, file):
        try:
            readCSV = pd.read_csv(file, sep=';', encoding='unicode_escape')
            for row in range(0, len(readCSV)):
                uploadStopwords = Daftar_stopwords(
                    stopwords = readCSV["Kata_stop"][row]
                )
                
                db.session.add(uploadStopwords)
            db.session.commit()
            
            flash("Berkas berhasil diimpor", "success")
        except Exception as e:
            flash(f"File failed to import", "danger")
            return e
    
    def create(self, *args):
        try:
            uploadStopword = Daftar_stopwords(
                stopwords = args[0]["stopwords"]
            )
            
            db.session.add(uploadStopword)
            db.session.commit()
            
            flash("Data berhasil disimpan", "success")
        except Exception as e:
            flash(f"Data failed to save", "danger")
            return e
    
    def retrieve(self):
        data_stopwords = Daftar_stopwords.query.order_by(Daftar_stopwords.stopwords).all()
        return data_stopwords
    
    def update(self, *args):
        try:
            slangUpdate = Daftar_stopwords.query.get_or_404(args[0]['id'])
          
            slangUpdate.stopwords = args[0]['stopwords']
            
            db.session.commit()
            flash("Data berhasil di ubah", "success")
        except Exception as e:
            flash("Data gagal di ubah", "danger")
            return e
    
    def delete(self, *args):
        try:
            stopHapus = Daftar_stopwords.query.get(args[0]['id'])

            db.session.delete(stopHapus)
            db.session.commit()
            flash("Data berhasil di hapus", "success")
        except Exception as e:
            flash("Data gagal di hapus", "danger")
            return e