import itertools


def main():
    letters = set(input().split('; '))
    line_length = int(input())

    for i in sorted([''.join(i) for i in itertools.permutations(list(letters), line_length)]):
        print(i)


if __name__ == '__main__':
    main()
