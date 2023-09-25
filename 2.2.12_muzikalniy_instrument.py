def main():
    a = int(input())
    b = int(input())
    c = int(input())

    if a + b > c:
        if a + c > b:
            if b + c > a:
                print('YES')
                return

    print('NO')


if __name__ == '__main__':
    main()
