def main():
    number = input()
    sum_digits = sum(map(int, list(number)))

    print(sum_digits)


if __name__ == '__main__':
    main()
