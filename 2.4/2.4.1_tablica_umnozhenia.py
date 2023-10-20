def main():
    target = int(input())

    for i in range(1, target + 1):
        for j in range(1, target + 1):
            print(i * j, end=' ')
        print()


if __name__ == '__main__':
    main()
