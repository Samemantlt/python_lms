def main():
    a, b = map(int, list(input()))
    c, d = map(int, list(input()))

    sorted_list = sorted([a, b, c, d])

    result = f'{sorted_list[3]}{(sorted_list[1] + sorted_list[2]) % 10}{sorted_list[0]}'

    print(result)


if __name__ == '__main__':
    main()
