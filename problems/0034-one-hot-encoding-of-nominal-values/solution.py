import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	if n_col is None:
		n_col = np.max(x) + 1
	
	res = np.zeros((len(x), n_col))
	for idx, value in enumerate(x):
		if 0 <= value < n_col:
			res[idx, value] = 1.0
	return res
