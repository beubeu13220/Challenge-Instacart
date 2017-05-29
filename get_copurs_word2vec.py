import os
import pandas as pd 
import numpy as np
from gensim.models import word2vec
from gensim.models import Doc2Vec, doc2vec
import utils
import time 
from collections import Counter
import pickle
import random

utils.data_directory()

order_products__prior = pd.read_csv("order_products__prior.csv")
order_products__train = pd.read_csv("order_products__train.csv")
order = pd.read_csv("orders.csv")

#prior
merge_order_product = pd.merge(order_products__prior[["order_id", "product_id", "reordered"]], 
                               order[["order_id", "user_id"]], on="order_id")
merge_order_product = merge_order_product[merge_order_product["reordered"]==1]
merge_order_product["product_id"] = merge_order_product["product_id"].astype("unicode")

#train
order_products__train = pd.merge(order_products__train, order[["order_id", "user_id"]],how="left", on="order_id")
order_products__train["product_id"] = order_products__train["product_id"].astype("unicode")
order_products__train = order_products__train[order_products__train["reordered"]==1]

liste_user = np.unique(order.ix[order["eval_set"]=="train", "user_id"])
n_user = len(liste_user)
thress = int(n_user*0.80)
random.shuffle(liste_user)
train_user = liste_user[:thress]
test_user = liste_user[thress:]



def words_for_user(data_prior, uid, train_mode, data_train):
    sequence = data_prior[data_prior["user_id"]==uid].groupby(["order_id"])["product_id"].apply(list)
    sequence = sequence.reset_index()["product_id"].tolist()

    if train_mode == True :
            train_sequence = data_train[data_train["user_id"]==uid].groupby(["order_id"])["product_id"].apply(list)
            sequence.append(train_sequence.reset_index()["product_id"].tolist())
    else :
        pass 
    
    return sequence

def label_for_user(uid, data_train):
    label = []
    test_sequence = data_train[data_train["user_id"]==uid].groupby(["order_id"])["product_id"].apply(list)
    label.append(test_sequence.reset_index()["product_id"].tolist())
    return label 

def saver_list(liste,name):
    with open(name, 'wb') as fp:
        pickle.dump(liste, fp)
    
    print("List saved")

start_time = time.time()
sentence_train = [words_for_user(merge_order_product, uid, True, order_products__train) for uid in train_user]
print("train end")
saver_list(sentence_train, "w2v_train")
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
sentence_test= [words_for_user(merge_order_product, uid, False, order_products__train) for uid in test_user]
print("test prior end")
saver_list(sentence_test, "w2v_test")
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
label_test= [label_for_user(uid, order_products__train) for uid in test_user]
print("test label end")
saver_list(label_test, "w2v_label_test")
print("--- %s seconds ---" % (time.time() - start_time))
