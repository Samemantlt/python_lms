def input_symbols() -> set:
    text = input()
    symbols = set()

    for symbol in text:
        symbols.add(symbol)
    
    return symbols


def main():
    word1 = input_symbols()
    word2 = input_symbols()

    print(''.join(word1.intersection(word2)))


if __name__ == '__main__':
    main()
