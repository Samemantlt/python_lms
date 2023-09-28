def main():
    height = int(input())
    width = int(input())

    digits = len(str(height * width))

    for x in range(height):
        for y in range(width):
            i = height * y + x + 1

            print(str(i).rjust(digits), end=" ")
            i += 1
        print()


if __name__ == '__main__':
    main()
