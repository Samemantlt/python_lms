def max_digit(num: int) -> int:
    return max(map(int, list(str(num))))


def main():
    n = int(input())

    for _ in range(n):
        number = int(input())
        dig = max_digit(number)
        print(dig, end="")


if __name__ == '__main__':
    main()
