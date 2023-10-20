def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    
    return a


def nok(a, b):
    return a * b // nod(a, b)


def main():
    a, b = int(input()), int(input())
    print(nok(a, b))


if __name__ == '__main__':
    main()
