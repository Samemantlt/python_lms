import itertools


def main():
    names = sorted([input() for _ in range(int(input()))])

    for t in itertools.permutations(names, 3):
        print(', '.join(list(t)))


if __name__ == '__main__':
    main()
