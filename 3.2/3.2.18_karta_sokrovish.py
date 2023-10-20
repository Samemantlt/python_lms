def calculate_starts(points: set) -> set:
    output = set()

    for x, y in points:
        output.add(f'{x // 10}{y // 10}')

    return output


def main():
    points = set()

    for _ in range(int(input())):
        line = input()
        x, y = map(int, line.split(' '))
        points.add((x, y))
    
    starts = calculate_starts(points)

    mmax = 0
    for start in starts:
        current = 0
        for x, y in points:
            if f'{x // 10}{y // 10}' == start:
                current += 1

        mmax = max(current, mmax)
    
    print(mmax)


if __name__ == '__main__':
    main()
