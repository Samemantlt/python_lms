import itertools


def main():
    n = int(input())
    names = [input() for i in range(n)]
    days = int(input())

    for name in itertools.islice(itertools.cycle(names), days):
        print(name)


if __name__ == '__main__':
    main()
