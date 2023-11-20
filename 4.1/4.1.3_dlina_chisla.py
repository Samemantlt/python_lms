import math


def number_length(num):
    return math.floor(math.log10(abs(num))) + 1


if __name__ == '__main__':
    main()
