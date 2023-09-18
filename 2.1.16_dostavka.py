def main():
    start = int(input())
    end = int(input())

    speed = int(input())

    print(f'{(end - start) / speed:.2f}')


if __name__ == '__main__':
    main()
