import math


def center_str(text: str, width: int):
    text_length = len(text)
    return math.floor((width - text_length) / 2) * ' ' + text + ' ' * math.ceil((width - text_length) / 2)


def main():
    count = int(input())
    size = int(input())

    for i in range(1, count + 1):
        for j in range(1, count):
            print(center_str(str(i * j), size), end='|')

        print(center_str(str(i * count), size))
        if i != count:
            print('-' * ((size + 1) * count - 1))


if __name__ == '__main__':
    main()
