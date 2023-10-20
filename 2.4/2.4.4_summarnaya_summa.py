def main():
    count = int(input())
    sum_digit = 0

    for _ in range(count):
        number = input()
        sum_digit += sum(map(int, list(number)))
    
    print(sum_digit)


if __name__ == '__main__':
    main()
