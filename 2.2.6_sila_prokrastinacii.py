def is_leap(year):
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

    return False


def main():
    year = int(input())

    print('YES' if is_leap(year) else 'NO')


if __name__ == '__main__':
    main()
