from app import db
from flask import flash, jsonify, json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from app.controllers.datacontroller import DataController
from app.controllers.tfidfcontroller import TfidfVectorizer
from app.controllers.mnbcontroller import MultiNB
import pandas as pd
import re

class TestingController:
    def __init__(self):
        self.data_clean = DataController().retrieveDataBefore()
        self.data_split = {'created_at': [], 'raw_tweets': [],'clean_tweets': [], 'label': []}
    
    def processTest(self, *args):
        rasio = float( args[0]['rasio'])
        
        for d in self.data_clean:
            self.data_split['created_at'].append(d.created_at)
            self.data_split['raw_tweets'].append(d.raw_tweets)
            self.data_split['clean_tweets'].append(d.clean_tweets)
            self.data_split['label'].append(d.label)
                
            
        X_train, X_test, y_train, y_test = train_test_split(self.data_split['raw_tweets'], self.data_split['label'], test_size = rasio, random_state = 0, stratify=self.data_split['label'])
            
        # tf = TfidfVectorizer()
        lb = LabelBinarizer()
        
        # text_tf = tf.fit_transform(self.data_split['clean_tweets']).toarray()
        label_lb = lb.fit_transform(self.data_split['label']).ravel()
        
        tfidf = TfidfVectorizer()
        
        tfidf.fit(self.data_split['clean_tweets'])
        text_tf = tfidf.transform(self.data_split['clean_tweets']).toarray()
        
        X_train1,X_test1,y_train1,y_test1 = train_test_split(text_tf, label_lb, test_size = rasio, random_state = 0, stratify=label_lb)
            
        mnb = MultiNB()
        mnb = mnb.fit(X_train1, y_train1)
        predicted = mnb.predict(X_test1)
        
        
        total_p = len([t for t in predicted if t == 1])
        total_n = len([t for t in predicted if t == 0])
        
        true_positif = 0
        true_negatif = 0
        false_positif = 0
        false_negatif = 0

        for i in range(len(predicted)):
            if predicted[i] == 1:
                if predicted[i] == y_test1[i]:
                    true_positif += 1
                else:
                    false_negatif += 1
            else:
                if predicted[i] == y_test1[i]:
                    true_negatif += 1
                else:
                    false_positif += 1

        predicted = list(predicted)
        predicted = [self.Analyze_score(x) for x in predicted]
        
        total = true_positif + true_negatif + false_positif + false_negatif
        accuration = ((true_positif + true_negatif) / (total))
        
        precision_p = (true_positif / (true_positif + false_positif))
        precision_n = (true_negatif / (true_negatif + false_negatif))
        
        precision_rate = ((precision_p + precision_n) / 2)
        
        recall_p = (true_positif / (true_positif + false_negatif))
        recall_n = (true_negatif / (true_negatif + false_positif))
        
        recall_rate = ((recall_p + recall_n) / 2)
        
        cmatrix = {
			'tpositif': true_positif,
			'tnegatif': true_negatif,
			'fpositif': false_positif,
			'fnegatif': false_negatif,
			'accuration': round(accuration, 2),
			'precision_p': round(precision_p, 2),
			'precision_n': round(precision_n, 2),
			'precision_rate': round(precision_rate, 2),
			'recall_p': round(recall_p, 2),
			'recall_n': round(recall_n, 2),
			'recall_rate': round(recall_rate, 2),
			'total_p': total_p,
			'total_n': total_n,
            'total': total
		}
        
        response = json.dumps({'X_train': list(X_train), 'X_test': list(X_test), 'y_train': list(y_train), 'y_test': list(y_test), 'predict': list(predicted), 'cmatrix': cmatrix})

        return response
    
    def Analyze_score(self, score):
        if score == 0:
            return 'Negatif'
        else:
            return "Positif"