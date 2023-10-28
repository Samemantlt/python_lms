import itertools


def main():
    words = sorted([word for _ in range(int(input())) for word in input().split(', ')])

    for a, b, c in itertools.permutations(words, 3):
        print(f'{a} {b} {c}')


if __name__ == '__main__':
    main()
