import pickle
import utils
from gensim.models import Doc2Vec, doc2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
utils.data_directory()

with open('D2v_test','rb') as f:
    sentences_test = pickle.load(f)
with open('D2v_train','rb') as f:
    sentences_train = pickle.load(f)   
with open('D2v_label_test','rb') as f:
    label_test = pickle.load(f) 
    
    
    
# Dbow
Docmodel = Doc2Vec(dm=0, dbow_words=1, window=3199, alpha=.025, min_alpha=.025, size=15, min_count=1, iter=10)
Docmodel.build_vocab(sentences_train)


Docmodel.train(sentences_train)

outfile = "test2"
Docmodel.save(outfile + '.model')
Docmodel.wv.save_word2vec_format(outfile + '.model.bin', binary=True)
Docmodel.wv.save_word2vec_format(outfile + '.model.txt', binary=False)
