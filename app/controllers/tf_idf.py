import math
from collections import Counter
from scipy.sparse import csr_matrix
from sklearn.preprocessing import normalize

class TfidfVectorizer:
    def __init__(self):
        self.idfs_ = {}
        self.vocab = {}
        
    def IDF(self, dataset, unique_words):
        idf_vals = {}
        total_docs = len(dataset) 
        for word in unique_words: 
            cnt = 0
            for row in dataset:
                if word in row.split(" "): 
                    cnt+=1 
            idf_vals[word] = 1 + math.log((1+total_docs)/(1+cnt)) 
        return idf_vals
    
    def fit(self, dataset):    
        unique_words = set() 
        if isinstance(dataset, (list,)):
            for row in dataset:
                for word in row.split(" "):
                    if len(word) < 2:
                        continue
                    unique_words.add(word)
            unique_words = sorted(list(unique_words))
            self.vocab = {j:i for i,j in enumerate(unique_words)}
        self.idfs_ = self.IDF(dataset, unique_words)
        return self.vocab, self.idfs_
    
    def transform(self, dataset):
        sparse_matrix = csr_matrix((len(dataset), len(self.vocab)), dtype=float)
        for row in range(0, len(dataset)):
            word_count = Counter(dataset[row].split(' '))
            for word in dataset[row].split(' '):
                if word in list(self.vocab.keys()):
                    tf = word_count[word] / len(dataset[row].split(' '))
                    tfidf = tf * self.idfs_[word]
                    sparse_matrix[row, self.vocab[word]] = tfidf
        self.tfidf_val = normalize(sparse_matrix, norm='l2', axis = 1, copy=True, return_norm=False)
        return self.tfidf_val
