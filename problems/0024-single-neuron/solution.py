import math
import numpy as np
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	features = np.array(features)
	weights = np.array((weights))
	labels = np.array(labels)
	z = features @ weights + bias
	predicted = 1 / (1 + np.exp(-z)) # [0, 1]
	mse = round((1/len(features)) * np.sum((predicted - labels)**2),4)
	probabilities = [round(float(p), 4) for p in predicted]
	return probabilities, mse