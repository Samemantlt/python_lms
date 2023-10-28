import itertools


def main():
    n = int(input())
    names = [input() for i in range(n)]

    for name1, name2 in itertools.combinations(names, 2):
        print(f'{name1} - {name2}')


if __name__ == '__main__':
    main()
