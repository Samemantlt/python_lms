def main():
    target = int(input())

    current = 0
    max_col = 1

    for i in range(1, target + 1):
        print(i, end=" ")
        current += 1
        if current == max_col:
            current = 0
            max_col += 1
            print()


if __name__ == '__main__':
    main()
