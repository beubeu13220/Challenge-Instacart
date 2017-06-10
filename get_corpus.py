import numpy as np
import pandas as pd
import pickle
import utils
from itertools import chain
from gensim.models import doc2vec
import time
# we choose the good directory according by the existing files

#Nombre de fois que le produit doit apparaitre
n = 8
#Nombre de produit qui doit contenir une commande 
w_min = 4
w_max = 35

utils.data_directory()

print("Import")
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
del order_products__train["add_to_cart_order"]

print("Merge")
# Merge 
df = pd.concat([merge_order_product, order_products__train], axis=0)
print("Shape initial : ", df.shape[0])  

# On supprime les produits acheté moins de n fois
df_produit = df.groupby(["product_id"])["order_id"].count().reset_index()
not_keep_product = df_produit.ix[df_produit["order_id"]<n, "product_id"].tolist()
df = df[~df["product_id"].isin(not_keep_product)]
print("Shape after filter product : ", df.shape[0])

# On supprime les commandes de moins de 3 élements ou plus 35 élements 
df_order = df.groupby(["order_id"])["product_id"].count().reset_index()
not_keep_order_min = df_order.ix[df_order["product_id"]<w_min, 'order_id'].tolist()
not_keep_order_max = df_order.ix[df_order["product_id"]>w_max, 'order_id'].tolist()
df = df[~df["order_id"].isin(not_keep_order_min)]
print("Shape after filter order min : ", df.shape[0])
df = df[~df["order_id"].isin(not_keep_order_max)]
print("Shape after filter order, final : ", df.shape[0])



print("Add order")
sequences = df.groupby(['order_id']).apply(lambda order : order['product_id'].tolist()).values

print("Save")    
with open('w2v_corpus_order', "wb") as fp:
    pickle.dump(sequences, fp)



