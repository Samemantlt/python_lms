import pandas as pd
import re
from typing import List
import numpy as np


RE_WORD = re.compile('[а-яА-Яa-zA-ZёЁ]+')


def get_words(text: str) -> List[str]:
    text = text.lower()
    words = []

    for match in RE_WORD.finditer(text):
        word = match.group(0)
        words.append(word)
    
    return words


def length_stats(text: str) -> pd.Series:
    words = set(get_words(text))
    dictionary0 = dict()
    dictionary1 = dict()

    for word in sorted(words):
        length = len(word)
        if length % 2 == 0:
            dictionary0[word] = length
        else:
            dictionary1[word] = length
    
    return pd.Series(dictionary1, dtype=np.int64), pd.Series(dictionary0, dtype=np.int64)
