def main():
    a = int(input())
    b = int(input())
    c = int(input())

    d = {
        a: 'Петя',
        b: 'Вася',
        c: 'Толя',
    }

    index = 1
    for i in sorted([a, b, c], reverse=True):
        print(f'{index}. {d[i]}')
        index += 1


if __name__ == '__main__':
    main()
