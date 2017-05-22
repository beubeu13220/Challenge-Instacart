def descr(data, n=5):
	print(data.shape)
	print(data.head(n))

def likely_format(number):
    return '{:,}'.format(number).replace(',', ' ')

    class MySentences(object):
    def __init__(self, name):
        self.name = name
        
    def run(self):
        sentence = []
        for i in range(self.name.shape[0]):
            sentence.append([self.name.ix[i, "order_id"], self.name.ix[i, "product_id"]])
        return sentence