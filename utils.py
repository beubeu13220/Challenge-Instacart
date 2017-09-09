import os 
import keras.backend as K

def descr(data, n=5):
    print(data.shape)
    print(data.head(n))

def likely_format(number):
    return '{:,}'.format(number).replace(',', ' ')


def data_directory():
    if os.path.exists("/home/ec2-user/data") :
        print("On AWS instance")
        os.chdir("/home/ec2-user/data")

    else :
        print("My local machine")
        os.chdir("/media/brehelin/0FECCBDE10E4BE99/Kaggle/Data")
        
    print(os.getcwd())


def pre_score(y_true, y_pred):

    # Count positive samples.
    c1 = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    c2 = K.sum(K.round(K.clip(y_pred, 0, 1)))
    c3 = K.sum(K.round(K.clip(y_true, 0, 1)))

    # If there are no true samples, fix the F1 score at 0.
    if c3 == 0:
        return 0
    return c1, c2, c3

def precision(y_true, y_pred):
    c1, c2, c3 = pre_score(y_true, y_pred)
    return c1/ c2

def recall(y_true, y_pred):
    c1, c2, c3 = pre_score(y_true, y_pred)
    return c1/ c3

def f1_score(y_true, y_pred):
    precision_s = precision(y_true, y_pred)
    recall_s = recall(y_true, y_pred)
    f1  = 2 * (precision_s * recall_s) / (precision_s + recall_s)
    return f1
    