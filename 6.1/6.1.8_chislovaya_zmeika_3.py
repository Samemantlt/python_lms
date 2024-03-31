import numpy as np


def snake(h, w, direction='H'):
    horizontal = direction == 'H'
    if horizontal:
        arr = np.arange(1, h * w + 1).reshape(w, h)
    else:
        arr = np.arange(1, h * w + 1).reshape(h, w)
    arr[1::2] = arr[1::2, ::-1]
    if horizontal:
        pass
    else:
        arr = arr.transpose()
    return arr.astype(np.int16)
