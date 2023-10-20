import itertools


def main():
    count = int(input())

    print('А Б В')
    for a, b, c in itertools.product(range(1, count - 2 + 1), repeat=3):
        if a + b + c != count:
            continue

        print(f'{a} {b} {c}')


if __name__ == '__main__':
    main()
