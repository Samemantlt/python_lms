def sum_digit(num: int) -> int:
    return sum(map(int, list(str(num))))


def main():
    kids_count = int(input())

    max_sum_digit_number = 0
    max_sum_digit_number_name = None

    for _ in range(kids_count):
        name = input()
        number = int(input())
        sum_dig = sum_digit(number)
        if sum_dig >= max_sum_digit_number:
            max_sum_digit_number = sum_dig
            max_sum_digit_number_name = name
    
    print(max_sum_digit_number_name)


if __name__ == '__main__':
    main()
