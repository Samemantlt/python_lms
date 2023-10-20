def main():
    N = int(input())
    M = int(input())
    T = int(input())

    M += T

    N += M // 60
    M = M % 60
    N %= 24

    print(f'{N:0>2}:{M:0>2}')


if __name__ == '__main__':
    main()
