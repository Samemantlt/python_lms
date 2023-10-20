def process_num(num: int) -> dict:
    bin_num = bin(num)[2:]

    return {
        'digits': len(bin_num),
        'units': bin_num.count('1'),
        'zeros': bin_num.count('0'),
    }


def main():
    nums = list(map(int, input().split(' ')))
    result = [process_num(num) for num in nums]

    print(result)


if __name__ == '__main__':
    main()
