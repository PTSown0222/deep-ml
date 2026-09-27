import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	scores = np.array(scores)
	max_score = np.max(scores)
	sum_score = np.log(np.sum(np.exp(scores - max_score)))
	return scores - max_score - sum_score