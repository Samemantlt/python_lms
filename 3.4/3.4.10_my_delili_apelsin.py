import itertools


def main():
    n = int(input())
    print(f'А Б В')
    for a, b, c in itertools.product(range(1, n - 2 + 1), repeat=3):
        if a + b + c != n:
            continue

        print(f'{a} {b} {c}')


if __name__ == '__main__':
    main()
