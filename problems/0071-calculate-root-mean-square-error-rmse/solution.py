import numpy as np

def rmse(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    if y_true.size == 0 or y_pred.size == 0:
        return 0.0
        
    n = y_pred.size
    rmse_res = np.sqrt(np.sum((y_true - y_pred) ** 2) / n)
    return round(float(rmse_res), 3)
