import itertools


def main():
    sequence = ('Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая')

    n = int(input())

    for i in range(n):
        print(sequence[i % len(sequence)])


if __name__ == '__main__':
    main()
