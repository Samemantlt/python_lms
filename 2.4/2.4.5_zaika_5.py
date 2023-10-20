def main():
    count = int(input())

    found = set()

    for i in range(count):
        while (item := input()) != 'ВСЁ':
            if item == 'зайка':
                found.add(i)

    print(len(found))


if __name__ == '__main__':
    main()
