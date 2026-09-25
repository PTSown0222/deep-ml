import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X_mat = np.array(X, dtype = float)
	y_mat = np.array(y, dtype = float).reshape(-1,1)
	# Normal Equation: theta = (X^T @ X)^(-1) @ X^T @ y
	theta = np.linalg.inv(X_mat.T @ X_mat) @ X_mat.T @ y_mat
	
	return np.round(theta.flatten(), 4).tolist()