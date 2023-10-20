def main():
    text = input()
    symbols = set()

    for symbol in text:
        symbols.add(symbol)
    
    print(''.join(symbols))


if __name__ == '__main__':
    main()
