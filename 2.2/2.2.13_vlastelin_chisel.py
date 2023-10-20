def main():
    a = set(list(input()))
    b = set(list(input()))
    c = set(list(input()))

    result = a.intersection(b).intersection(c)

    print(next(iter(result)))


if __name__ == '__main__':
    main()
