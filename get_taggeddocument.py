
##############################################

# get the list of user id with her word list #

##############################################

"""
How launch this script in back task
>>> nohup python get_taggeddocument.py &
to see all processus that run in back task 
>>> ps
"""
import numpy as np
import pandas as pd 
import pickle 
import utils
from gensim.models import doc2vec
import time 
# we choose the good directory according by the existing files
utils.data_directory()


# We load the two datasets that we need 
order_products__prior = pd.read_csv("order_products__prior.csv")
order = pd.read_csv("orders.csv")

# We merge their to get the final dataset
# and apply the code type 
merge_order_product = pd.merge(order_products__prior[["order_id", "product_id"]], 
                               order[["order_id", "user_id"]], on="order_id")
merge_order_product["product_id"] = merge_order_product["product_id"].astype("unicode")

# function to get the the word list for each user_id
def words_for_user(uid):
    return merge_order_product.ix[merge_order_product["user_id"]==uid, "product_id"].tolist()

liste_unique_user = list(np.unique(merge_order_product["user_id"]))
print("nb unique user :", len(liste_unique_user))

# Iteration on each user_id and generate a taggeddocument object
# we add it in a list, this format is usefull for the Doc2Vec model
start_time = time.time()
sentences = [doc2vec.TaggedDocument(words=words_for_user(uid), tags=[uid]) for uid in liste_unique_user]
print("--- %s seconds ---" % (time.time() - start_time))

# Like the execution is very long, we save the list object with pickel
# after we can load the list when we want 


with open('TaggedDocument', 'wb') as fp:
    pickle.dump(sentences, fp)
    
print("List saved")
