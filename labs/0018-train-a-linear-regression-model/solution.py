import numpy as np

def train(X, y, W, b):
    """
    Train linear regression weights on standardized data.
    
    Args:
        X: numpy array of shape (n_samples, n_features) -- standardized features
        y: numpy array of shape (n_samples,) -- standardized targets
        W: numpy array of shape (n_features,) -- initial random weights
        b: float -- initial bias (0.0)
    
    Returns:
        W: numpy array of shape (n_features,) -- trained weights
        b: float -- trained bias
    """
    # TODO: implement your training strategy here
    # You can use ANY approach: gradient descent, normal equation,
    # momentum, adaptive learning rates, mini-batching, etc.
    n = X.shape[0]
    lr = 0.01
    num_iterations = 1000

    X_numpy = np.array(X)
    y_numpy = np.array(y)
    for _ in range(num_iterations):
        predict = X_numpy @ W[:, np.newaxis] + b
        loss = predict.reshape(-1) - y_numpy
        dW = (2 / n) * (X_numpy.T @ loss)
        db = (2 / n) * np.sum(loss) # scaler
        W = W - lr * dW
        b = b - lr * db
    return W, b
