def main():
    N = int(input())
    M = int(input())

    p = 7 - 3 + 2 + N
    v = 6 + 3 + M

    print('Петя' if p > v else 'Вася')


if __name__ == '__main__':
    main()
