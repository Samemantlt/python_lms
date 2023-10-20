def is_palindrom(a: object):
    a = str(a)
    return a == a[::-1]


def main():
    count = int(input())
    result = 0

    for _ in range(count):
        number = int(input())
        if is_palindrom(number):
            result += 1

    print(result)


if __name__ == '__main__':
    main()
