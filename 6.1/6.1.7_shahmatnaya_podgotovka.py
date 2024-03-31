import numpy as np


def make_board(n):
    line = np.arange(0, n) % 2

    return ((line ^ line[:, None] + 1) % 2).astype(np.int8)
