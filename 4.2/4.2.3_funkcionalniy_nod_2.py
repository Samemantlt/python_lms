def _gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    
    return a


def gcd(*values):
    num = values[0]
    
    for v in values[1:]:
        num = _gcd(num, v)

    return num


if __name__ == '__main__':
    main()
