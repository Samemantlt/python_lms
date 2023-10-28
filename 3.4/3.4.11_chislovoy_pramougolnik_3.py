import itertools
import math


def main():
    h = int(input())
    w = int(input())

    target_length = math.floor(math.log10(h * w)) + 1

    last_y = None
    for y, x in itertools.product(range(h), range(1, w + 1)):
        if y != last_y:
            if last_y is not None:
                print()
            last_y = y
        print(str(y * w + x).rjust(target_length), end=' ')


if __name__ == '__main__':
    main()
