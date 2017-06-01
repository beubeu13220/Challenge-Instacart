import numpy as np
import pandas as pd 
import pickle 
import utils
from itertools import chain
from gensim.models import doc2vec
import time 
# we choose the good directory according by the existing files
utils.data_directory()


# We load the two datasets that we need 
order_products__prior = pd.read_csv("order_products__prior.csv")
order_products__train = pd.read_csv("order_products__train.csv")
order = pd.read_csv("orders.csv")
#PRIOR
merge_order_product = pd.merge(order_products__prior[["order_id", "product_id", "reordered"]], 
                               order[["order_id", "user_id"]], on="order_id")
merge_order_product = merge_order_product[merge_order_product["reordered"]==1]
merge_order_product["product_id"] = merge_order_product["product_id"].astype("unicode")

#TRAIN
order_products__train = pd.merge(order_products__train, order[["order_id", "user_id"]],how="left", on="order_id")
order_products__train["product_id"] = order_products__train["product_id"].astype("unicode")
order_products__train = order_products__train[order_products__train["reordered"]==1]

# function to get the the word list for each user_id
def words_for_user(data_prior, uid):
    sequence = data_prior[data_prior["user_id"]==uid].groupby(["order_id"])["product_id"].apply(list)
    return list(chain(*sequence.reset_index()["product_id"].values))

def label_for_user(data, uid):
    return data[data["user_id"]==uid]["product_id"].tolist()

liste_unique_user = list(merge_order_product["user_id"].unique())
print("nb unique user :", len(liste_unique_user))

start_time = time.time()
sentences = [words_for_user(merge_order_product, uid) for uid in liste_unique_user]
print("--- %s seconds ---" % (time.time() - start_time))

with open('w2v_corpus_prior', 'wb') as fp:
    pickle.dump(sentences, fp)
with open('w2v_uid_prior', 'wb') as fp:
    pickle.dump(liste_unique_user, fp)
     
print("Corpus saved")

start_time = time.time()
label = [label_for_user(order_products__train, uid) for uid in liste_unique_user]
print("--- %s seconds ---" % (time.time() - start_time))

with open('w2v_corpus_label', 'wb') as fp:
    pickle.dump(label, fp)
     
print("Label saved")
