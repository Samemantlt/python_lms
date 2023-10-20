def main():
    height = int(input())
    width = int(input())

    digits = len(str(height * width))

    for y in range(height):
        to_rev = y % 2 != 0
        for x in reversed(range(width)) if to_rev else range(width):
            i = y * width + x + 1

            print(str(i).rjust(digits), end=" ")
            i += 1
        print()


if __name__ == '__main__':
    main()
