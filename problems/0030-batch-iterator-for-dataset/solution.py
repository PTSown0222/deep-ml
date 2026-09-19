import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	samples = len(X)
	batches = []
	for i in range(0, samples, batch_size):
		batch_x = X[i: i + batch_size]
		if y is not None:
			batch_y = y[i: i + batch_size]
			batches.append([batch_x, batch_y])
		else:
			batches.append(batch_x)
	return batches