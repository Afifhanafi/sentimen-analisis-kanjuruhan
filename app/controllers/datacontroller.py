from app import db
from flask import flash
from app.models import DatasetBefore, DatasetAfter
import pandas as pd

#Dataset Sebelum Tragedi Kanjuruhan
class DataController:
    def importDataset(self, file, model):
        try:
            readCSV = pd.read_csv(file, sep=';', encoding='unicode_escape')
            for row in range(0, len(readCSV)):
                dataset = model(
                    created_at = readCSV["created_at"][row],
                    username = readCSV["username"][row],
                    label = readCSV["label"][row],
                    raw_tweets = readCSV["tweet"][row]
                )
                
                db.session.add(dataset)
            db.session.commit()
            
            flash("Berkas berhasil diimpor", "success")
        except Exception as e:
            flash(f"File failed to import", "danger")
            return e
    
    def retrieveCountData(self, model):
        return model.query.count()
    
    def retrieveData(self, model):
        return model.query.all()
    
    def retrieveJSON(self, model):
        dataset = self.retrieveData(model)
    
        headersData = ['id', 'created_at', 'username', 'raw_tweets', 'clean_tweets', 'label']
        
        dataJson = []
        for result in dataset:
            rs = [str(result.id),str(result.created_at), str(result.username), str(result.raw_tweets),str(result.clean_tweets), str(result.label)]
            dataJson.append(dict(zip(headersData,rs)))
            
        return { 'data': dataJson }