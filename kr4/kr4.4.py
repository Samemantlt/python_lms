def counter(text: str):
    symbols = {symbol for symbol in text if symbol.isalpha()}
    
    symbols = sorted(symbols)

    for symbol in symbols:
        yield symbol, text.count(symbol)
