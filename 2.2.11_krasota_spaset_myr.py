def main():
    a, b, c = sorted(map(int, list(input())))
    if (a + c) == b * 2:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
