ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def process_symb(symbol: str, offset: int):
    if not symbol.isalpha():
        return symbol
    
    isupper = symbol.isupper()
    letter = ALPHABET[(ALPHABET.index(symbol.upper()) + offset) % len(ALPHABET)]

    return letter if isupper else letter.lower()


def main():
    offset = int(input())

    with open('public.txt') as file:
        text = file.read()
    
    private_text = ''.join([process_symb(symbol, offset) for symbol in text])

    filename = 'private.txt'
    with open(filename, 'w') as file:
        file.write(private_text)


if __name__ == '__main__':
    main()
