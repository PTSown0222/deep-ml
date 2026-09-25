import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	muy = np.mean(data, axis=0, keepdims=True)
	var = np.std(data, axis=0, keepdims=True)
	standardized_data = np.round((data - muy) / var, 4)
	# Min-Max Normalization
	x_min = np.min(data, axis=0, keepdims=True)
	x_max = np.max(data, axis=0, keepdims=True)
	normalized_data = np.round((data - x_min) / (x_max - x_min), 4)
	return standardized_data, normalized_data