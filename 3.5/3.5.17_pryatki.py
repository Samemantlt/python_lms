def main():
    with open('secret.txt') as file:
        text = file.read()
    
    for symbol in text:
        print(chr(ord(symbol) % 256), end='')


if __name__ == '__main__':
    main()
