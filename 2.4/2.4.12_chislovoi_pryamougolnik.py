def main():
    height = int(input())
    width = int(input())

    digits = len(str(height * width))

    i = 1
    for _ in range(height):
        for _ in range(width):
            print(str(i).rjust(digits), end=" ")
            i += 1
        print()


if __name__ == '__main__':
    main()
