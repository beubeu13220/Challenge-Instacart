def descr(data, n=5):
	print(data.shape)
	print(data.head(n))

def likely_format(number):
    return '{:,}'.format(number).replace(',', ' ')