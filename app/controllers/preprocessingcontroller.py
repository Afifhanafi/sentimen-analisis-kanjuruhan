from app import db
from flask import flash, jsonify, json
from app.models import DatasetBefore, DatasetAfter
from app.controllers.datacontroller import DataController
from app.controllers.slangwordcontroller import SlangwordController
from app.controllers.stopwordcontroller import StopwordController
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import pandas as pd
import re

class PreprocessingController:
    def __init__(self):
        self.awal_data = []
        self.caseFolding_data = []
        self.cleansing_data = []
        self.slangwords_data = []
        self.stopwordsRemoval_data = []
        self.stemming_data = []
        self.data_akhir = []
        self.slang_headers = ['slangwords', 'kata_baku']
        self.stopwords_headers = ['stopwords']
        self.raw_headers = ['id', 'created_at', 'username', 'raw_tweets', 'clean_tweets']
    
    def process(self, model):
        data = DataController().retrieveData(model)
        
        data_raw=[]
        for result in data:
            rs = [str(result.id), str(result.created_at), str(result.username), str(result.raw_tweets), str(result.clean_tweets)]
            data_raw.append(dict(zip(self.raw_headers,rs)))

        data_save = {'id':[], 'created_at': [], 'username': [], 'raw_tweets': [],'clean_tweets': []}

        slangdb = SlangwordController().retrieve()
        
        data_slang = []
        for result in slangdb:
            rs = [str(result.kata_slang), str(result.kata_baku)]
            data_slang.append(dict(zip(self.slang_headers,rs)))

        stopwordsdb = StopwordController().retrieve()
        
        data_stopwords = []
        for result in stopwordsdb:
            rs = [str(result.stopwords)]
            data_stopwords.append(dict(zip(self.stopwords_headers,rs)))
            
        instance_Stemming = StemmerFactory()
        stemmer = instance_Stemming.create_stemmer()

        print('\n-- PROSES '+ str(len(data_raw)) +' DATA --')
        for index, data in enumerate(data_raw):
            self.awal_data.append(data['raw_tweets'])
            
            # Case Folding : Mengubah huruf menjadi huruf kecil
            hasil_data = data['raw_tweets'].lower()
            self.caseFolding_data.append(hasil_data)
            
            # === Menghapus Tautan ===
            hasil_data = re.sub("\w+:\/\/\S+"," ", hasil_data)
            
            # === Menghapus karakter selain huruf ===
            
            # Menghilangkan mention, hashtag, character reference
            hasil_data = re.sub('[@#&][A-Za-z0-9_]+'," ", hasil_data)
            
            # Menghilangkan tanda baca
            hasil_data = re.sub('[()!?;,]', ' ', hasil_data)
            hasil_data = re.sub('\[.*?\]',' ', hasil_data)

            # Menghilangkan tanda selain huruf
            hasil_data = re.sub("[^a-z]"," ", hasil_data)
            
            # === Menghapus 1 karakter ===
            hasil_data = re.sub(r"\b[a-z]\b", "", hasil_data)
            
            # Menghilangkan spasi lebih dari 1
            hasil_data = ' '.join(hasil_data.split())
            self.cleansing_data.append(hasil_data)
            
            # Merubah slang word ke kata aslinya
            for slang in data_slang:
                if slang['slangwords'] in hasil_data:
                    hasil_data = re.sub(r'\b{}\b'.format(slang['slangwords']), slang['kata_baku'], hasil_data)
            self.slangwords_data.append(hasil_data)

            # Menghapus stop word
            for stop in data_stopwords:
                if stop['stopwords'] in hasil_data:
                    hasil_data = re.sub(r'\b{}\b'.format(stop['stopwords']), '', hasil_data)
            self.stopwordsRemoval_data.append(hasil_data)
            
            hasil_data = stemmer.stem(hasil_data)
            self.stemming_data.append(hasil_data)
            
            self.data_akhir.append(hasil_data)
            
            
            print(index+1)
        
        # Simpan tweets ke database
        for i in range(0, len(self.data_akhir)+1):
            dataset = model.query.filter_by(id=i).update({model.clean_tweets : self.data_akhir[i-1]})
            
            db.session.commit()
                
        print('\n-- SELESAI --\n')
        
        # Menampilkan data ke layar
        response = json.dumps({'awal_data': self.awal_data, 'caseFolding_data': self.caseFolding_data, 'cleansing_data': self.cleansing_data, 'slangwords_data': self.slangwords_data, 'stopwordsRemoval_data': self.stopwordsRemoval_data, 'stemming_data': self.stemming_data})
        return response