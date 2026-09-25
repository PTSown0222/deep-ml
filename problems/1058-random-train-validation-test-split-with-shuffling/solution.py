import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    # Your code here
    if train_frac + validation_frac > 1:
        raise Exception("train_frac + validation_frac must be lesser than 1")
    n = data.shape[0]
    indices = np.random.default_rng(seed).permutation(n)
    train_end = int(n * train_frac)
    validation_end = train_end + int(n * validation_frac)
    train = data[indices[:train_end]]
    validation = data[indices[train_end:validation_end]]
    test = data[indices[validation_end:]]
    return [train, validation, test]