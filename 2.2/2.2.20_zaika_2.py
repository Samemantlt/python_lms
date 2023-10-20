def main():
    a = input()
    b = input()
    c = input()

    lines = [a, b, c]
    lines = list(filter(lambda a: 'зайка' in a, lines))
    
    m = min(lines)

    print(f'{m} {len(m)}')


if __name__ == '__main__':
    main()
