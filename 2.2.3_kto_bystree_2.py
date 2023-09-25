def main():
    a = int(input())
    b = int(input())
    c = int(input())

    if a == max(a, b, c):
        print('Петя')

    if b == max(a, b, c):
        print('Вася')

    if c == max(a, b, c):
        print('Толя')


if __name__ == '__main__':
    main()
