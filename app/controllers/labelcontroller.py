from app import db
from flask import flash
from app.models import DatasetBefore, DatasetAfter
import pandas as pd

class LabelController:
    def __init__(self, *args):
        if args:
            self.id = args[0]["id"]
            self.value = args[0]["value"]
    
    def updateDataset(self, model):
        update_label = model().query.get(self.id)
        update_label.label = self.value
        
        db.session.commit()
    
    def updateDatasetAfter(self):
        pass