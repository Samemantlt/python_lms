import numpy as np


def stairs(arr: np.ndarray):
    result = np.tile(arr, arr.size).reshape(arr.size, arr.size)
    for i in range(1, arr.shape[0] + 1):
        result[i,:] = np.roll(result[i,:], i)
    return result


print(stairs(np.arange(3)))