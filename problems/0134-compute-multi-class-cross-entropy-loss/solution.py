import numpy as np

def compute_cross_entropy_loss(predicted_probs: np.ndarray, true_labels: np.ndarray, epsilon = 1e-15) -> float:
    preds_clipped = np.clip(predicted_probs, epsilon, 1 - epsilon)
    loss = -np.sum(true_labels * np.log(preds_clipped)) / predicted_probs.shape[0]
    return loss