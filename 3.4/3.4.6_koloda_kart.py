import itertools


def main():
    to_skip = input()

    values = [
        *[str(i) for i in range(2, 10 + 1)],
        'валет',
        'дама',
        'король',
        'туз',
    ]

    categories = [
        'пик',
        'треф',
        'бубен',
        'червей'
    ]
    categories.remove(to_skip)

    for v, c in itertools.product(values, categories):
        print(f'{v} {c}')


if __name__ == '__main__':
    main()
