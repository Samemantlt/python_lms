def main():
    text = input()

    last_symbol = None
    current_count = 0
    for symbol in text:

        if last_symbol != symbol:
            if last_symbol is not None:
                print(f'{last_symbol} {current_count}')
            
            last_symbol = symbol
            current_count = 0
            
        current_count += 1

    if current_count != 0:
        print(f'{last_symbol} {current_count}')
    

if __name__ == '__main__':
    main()
