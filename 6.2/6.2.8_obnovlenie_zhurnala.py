import pandas as pd


def update(data: pd.Series):
    result = data.copy()
    result["average"] = (result["maths"] + result["physics"] + result["computer science"]) / 3
    result = result.sort_values(['average', 'name'], ascending=[False, True])
    return result
