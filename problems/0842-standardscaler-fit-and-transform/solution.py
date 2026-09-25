import numpy as np

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """
    Fit a standard scaler on X_train and transform X_test.
    Returns the standardized X_test as a numpy array.
    """
    mu = np.mean(X_train, axis = 0, keepdims = True)
    sigma = np.std(X_train, axis = 0, keepdims = True)
    # filter of sigma == 0 we assgin = 1.0
    sigma[sigma == 0] = 1.0
    X_test_scaled = (X_test - mu) / sigma
    return X_test_scaled

