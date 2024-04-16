import pandas as pd


def discount(arg: pd.DataFrame):
    cheque = arg.copy(True)
    
    sl = cheque[cheque["number"] > 2]
    sl["cost"] = sl["cost"] / 2
    
    cheque[cheque["number"] > 2] = sl

    return cheque


def cheque(price_list: pd.Series, **kwargs):
    products = []
    prices = []
    numbers = []
    costs = []

    for name, value in sorted(kwargs.items(), key=lambda a: a[0]):
        products.append(name)
        prices.append(price_list[name])
        numbers.append(value)
        costs.append(price_list[name] * value)
    
    return pd.DataFrame({
        "product": products,
        "price": prices,
        "number": numbers,
        "cost": costs,
    })
