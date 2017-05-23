import os 

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

    