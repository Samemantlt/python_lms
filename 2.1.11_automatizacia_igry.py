def main():
    num = input() # abcd -> badc

    a, b, c, d = list(num)
    print(f'{b}{a}{d}{c}')


if __name__ == '__main__':
    main()
