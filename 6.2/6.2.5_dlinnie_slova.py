import pandas as pd
import numpy as np


def get_long(words: pd.Series, min_length: int = 5):
    return words.loc[lambda x: x >= min_length]
