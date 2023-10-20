def main():
    n = int(input())
    count = 0

    for _ in range(n):
        if 'зайка' in input():
            count += 1
    
    print(count)


if __name__ == '__main__':
    main()
