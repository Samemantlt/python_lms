def main():
    start, end = int(input()), int(input())

    for i in range(start, end + 1) if start <= end else range(start, end - 1, -1):
        print(i, end=" ")


if __name__ == '__main__':
    main()
