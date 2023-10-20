def main():
    a, b, c = map(int, list(input()))
    left = a + b
    right = b + c

    print(f'{max(left, right)}{min(left, right)}')


if __name__ == '__main__':
    main()
