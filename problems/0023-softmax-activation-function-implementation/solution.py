import math
import numpy as np
def softmax(scores: list[float]) -> list[float]:
    scores = np.array(scores)
    max_z = np.max(scores)
    top = np.exp(scores - max_z)
    bot = np.sum(np.exp(scores-max_z), keepdims = True)
    result = top/bot
    return result