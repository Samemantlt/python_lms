def sum_digit(num: int) -> int:
    return sum(map(int, list(str(num))))


def to_ss(number: int, base: int) -> str:
    result = ''

    while number != 0:
        result += str(number % base)
        number //= base
    
    return result[::-1]


def main():
    number = int(input())

    max_digit = 0
    max_digit_ss = -1

    for i in range(10, 2 - 1, -1):
        converted = to_ss(number, i)
        current = sum_digit(converted)

        if current >= max_digit:
            max_digit = current
            max_digit_ss = i
    
    print(max_digit_ss)


if __name__ == '__main__':
    main()
