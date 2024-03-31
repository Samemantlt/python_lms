import numpy as np


def rotate(arr: np.ndarray, angle: int):
    angle = 360 - angle
    while angle > 0:
        arr = np.rot90(arr)
        angle -= 90
    
    return arr
