def custom_hash(m, r, h_previous):
    return 37 * (m + r + h_previous) % 256


# m, r, h
def parse_block(number: int) -> tuple:
    return (number >> 16) & 0xFF, (number >> 8) & 0xFF, number & 0xFF


def main():
    h_previous = 0
    count = int(input())

    blocks = []

    for i in range(count):
        block = int(input())
        blocks.append(block)

    for i in range(count):
        m, r, h = parse_block(blocks[i])

        real_h = custom_hash(m, r, h_previous)
        if h != real_h:
            print(i)
            exit()
        if h >= 100:
            print(i)
            exit()

        h_previous = h

    print(-1)


if __name__ == '__main__':
    main()
