# def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
# 	import numpy as np
# 	flag = False
# 	if mode == "column":
# 		means = np.mean(matrix, axis = 0)
# 		flag = True
# 	elif mode == "row":
# 		means = np.mean(matrix, axis = 1)
# 		flag = True
# 	return means if flag else False

def calculate_matrix_mean(matrix, mode):
	if not matrix or not matrix[0]:
		return []
	
	num_rows = len(matrix)
	num_cols = len(matrix[0])

	if mode == "row":
		means = []
		for row in matrix:
			row_mean = sum(row) / len(row)
			means.append(row_mean)
		return means
	elif mode == "column":
		means = []
		for col_idx in range(num_cols):
			col_sum = 0
			for row_idx in range(num_rows):
				col_sum += matrix[row_idx][col_idx]
			means.append(col_sum / num_rows)
		return means
	return []