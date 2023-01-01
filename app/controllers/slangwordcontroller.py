from app import db
from flask import flash
from app.models import Daftar_slangwords
import pandas as pd

class SlangwordController:
    def importData(self, file):
        try:
            readCSV = pd.read_csv(file, sep=';', encoding='unicode_escape')
            for row in range(0, len(readCSV)):
                uploadSlangwords = Daftar_slangwords(
                    kata_slang = readCSV["Kata_slang"][row],
                    kata_baku = readCSV["Kata_baku"][row]
                )
                
                db.session.add(uploadSlangwords)
            db.session.commit()
            
            flash("Berkas berhasil diimpor", "success")
        except Exception as e:
            flash(f"File failed to import", "danger")
            return e
    
    def create(self, *args):
        try:
            uploadSlangword = Daftar_slangwords(
                kata_slang = args[0]["slangword"],
                kata_baku = args[0]["kata_baku"]
            )
            
            db.session.add(uploadSlangword)
            db.session.commit()
            
            flash("Data berhasil disimpan", "success")
        except Exception as e:
            flash(f"Data failed to save", "danger")
            return e
    
    def retrieve(self):
        data_slangwords = Daftar_slangwords.query.order_by(Daftar_slangwords.kata_slang).all()
        return data_slangwords
    
    def update(self, *args):
        try:
            slangUpdate = Daftar_slangwords.query.get_or_404(args[0]['id'])
          
            slangUpdate.kata_slang = args[0]['slangword']
            slangUpdate.kata_baku = args[0]['kata_baku']
            
            db.session.commit()
            flash("Data berhasil di ubah", "success")
        except Exception as e:
            flash("Data gagal di ubah", "danger")
            return e
    
    def delete(self, *args):
        try:
            slangHapus = Daftar_slangwords.query.get(args[0]['id'])

            db.session.delete(slangHapus)
            db.session.commit()
            flash("Data berhasil di hapus", "success")
        except Exception as e:
            flash("Data gagal di hapus", "danger")
            return e