import numpy as np
from collections import Counter
import math
def dummy_classifier(y_train, n_test, strategy, constant=None):
    """
    Produce baseline predictions of length n_test using the given strategy.
    Returns a Python list of predicted labels.
    """
    sorted_classes = sorted(list(set(y_train)))
    if strategy == "constant":
        return [constant] * n_test
    elif strategy == "most_frequent":
        counts = Counter(y_train)
        most_common = sorted(counts.items(), key=lambda x: (-x[1], x[0]))[0][0]
        return [most_common] * n_test
    elif strategy == "uniform":
        k = len(sorted_classes)
        return [sorted_classes[i % k] for i in range(n_test)]
    elif strategy == "stratified":
        n_train = len(y_train)
        counts = Counter(y_train)

        allocations = {}
        remainders = []
        for c in sorted_classes:
            f_c = counts[c] / n_train
            exact_count = n_test * f_c
            base_count = math.floor(n_test * f_c)
            allocations[c] = base_count
            fractional_part = exact_count - base_count
            remainders.append((fractional_part, c))
        
        current_total = sum(allocations.values())
        deficit = n_test - current_total
        remainders.sort(key=lambda x: (-x[0], x[1]))

        for i in range(deficit):
            c = remainders[i][1]
            allocations[c] += 1
        predictions = []
        for c in sorted_classes:
            predictions.extend([c] * allocations[c])
        return predictions
    return []


