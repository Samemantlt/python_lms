def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


def main():
    number = int(input())

    print(factorial(number))


if __name__ == '__main__':
    main()
