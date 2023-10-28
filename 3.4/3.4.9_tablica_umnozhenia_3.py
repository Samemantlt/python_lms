import itertools


def main():
    n = int(input())

    for _, values in itertools.groupby(itertools.product(range(1, n + 1), range(1, n + 1)), key=(lambda a: a[0])):
        print(' '.join([str(x * y) for x, y in values]))


if __name__ == '__main__':
    main()
