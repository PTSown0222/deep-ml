import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	a = np.array(a)
	row, col = new_shape
	if a.shape[0] * a.shape[1] != row * col:
		return []
	reshaped_matrix = a.reshape(a.shape[1], a.shape[0])
	return reshaped_matrix.tolist()