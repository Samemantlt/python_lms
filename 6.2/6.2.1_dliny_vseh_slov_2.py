import pandas as pd
import re
from typing import List


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
    dictionary = dict()

    for word in sorted(words):
        dictionary[word] = len(word)
    
    return pd.Series(dictionary)
