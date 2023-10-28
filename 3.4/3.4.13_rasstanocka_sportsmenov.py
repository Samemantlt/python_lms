import itertools


def main():
    names = [input() for _ in range(int(input()))]

    for t in itertools.permutations(names):
        print(', '.join(list(t)))


if __name__ == '__main__':
    main()
