def main():
    num1 = int(input())
    num2 = int(input())

    def get_digit(num, index):
        text = str(num)
        if index > len(text):
            return 0
        return int(text[-index])

    def d_sum(index):
        return (get_digit(num1, index) + get_digit(num2, index)) % 10

    res = f'{d_sum(4)}{d_sum(3)}{d_sum(2)}{d_sum(1)}'

    print(int(res))


if __name__ == '__main__':
    main()
