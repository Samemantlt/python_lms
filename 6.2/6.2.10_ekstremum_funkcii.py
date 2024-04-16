import numpy as np
import pandas as pd


def values(func, start, end, step) -> pd.Series:
    index = np.arange(start, end + step, step)
    vals = np.vectorize(func)(index)

    return pd.Series(vals, index=index, dtype=np.float64)


def min_extremum(data: pd.Series) -> float:
    return data.idxmin()


def max_extremum(data: pd.Series) -> float:
    return data.idxmax()
