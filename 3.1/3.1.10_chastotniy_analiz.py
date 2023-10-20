def main():
    symbols = dict()

    while True:
        text = input()
        if text == 'ФИНИШ':
            break

        for symbol in text:
            if symbol == ' ':
                continue

            symbol = symbol.lower()
            if symbol not in symbols:
                symbols[symbol] = 0
                
            symbols[symbol] += 1
    
    m_key, m_value = None, 0
    for key, value in symbols.items():
        if value > m_value:
            m_value = value
            m_key = key
    
    print(m_key)


if __name__ == '__main__':
    main()
