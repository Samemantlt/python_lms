def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        elif b > a:
            b -= a

    return a


if __name__ == '__main__':
    main()
