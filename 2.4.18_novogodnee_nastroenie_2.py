import math


def count_rows(count):
    result = 0

    while count > 0:
        result += 1
        count -= result
    
    return result


def center_str(text: str, width: int):
    text_length = len(text)
    return math.floor((width - text_length) / 2) * ' ' + text + ' ' * math.ceil((width - text_length) / 2)


def main():
    count = int(input())

    rows_count = count_rows(count)

    max_col = 1

    i = 1
    rows = []

    for _ in range(rows_count):
        row = []

        for _ in range(max_col):
            row.append(i)
            i += 1

            if i > count:
                break
        
        max_col += 1
        rows.append(' '.join(map(str, row)))

    row_width = max(map(len, rows))

    for row in rows:
        print(center_str(row, row_width))


if __name__ == '__main__':
    main()
