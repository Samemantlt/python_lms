import math


def center_str(text: str, width: int):
    text_length = len(text)
    return math.floor((width - text_length) / 2) * ' ' + text + ' ' * math.ceil((width - text_length) / 2)


def main():
    target = math.ceil(int(input()) / 2)
    digits = len(str(target)) + 1

    for i in range(1, target + 1):
        for j in range(1, target + 1):
            print(center_str(str(min(j, i)), digits), end='')
        for j in range(target - 1, 0, -1):
            print(center_str(str(min(j, i)), digits), end='')
        print()

    for i in range(target - 1, 0, -1):
        for j in range(1, target + 1):
            print(center_str(str(min(j, i)), digits), end='')
        for j in range(target - 1, 0, -1):
            print(center_str(str(min(j, i)), digits), end='')
        print()


if __name__ == '__main__':
    main()
