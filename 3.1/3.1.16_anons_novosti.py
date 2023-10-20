def main():
    max_length = int(input())
    n_lines = int(input())

    lines = []

    for _ in range(n_lines):
        line = input()
        lines.append(line)

    for i, line in enumerate(lines):
        if len(line) < max_length - 3:
            print(line)
            max_length -= len(line)
        elif len(line) == max_length and i == len(lines) - 1:
            print(line)
        else:
            print(line[:max_length - 3] + '...')
            break


if __name__ == '__main__':
    main()
