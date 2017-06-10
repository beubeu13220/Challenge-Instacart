import pandas as pd
import numpy as np
import utils
import pickle
import logging
from gensim.models import word2vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
utils.data_directory()

with open('w2v_corpus_order','rb') as f:
    sentences = pickle.load(f)   
    
    
window = len(max(sentences,key=len))

model = word2vec.Word2Vec(sentences, size=20, window=window, min_count=1, workers=1, iter=20, sample=1e-4, negative=20)
model.train(sentences)


outfile = "test1"
model.save(outfile + '.model')
model.wv.save_word2vec_format(outfile + '.model.bin', binary=True)
model.wv.save_word2vec_format(outfile + '.model.txt', binary=False)
