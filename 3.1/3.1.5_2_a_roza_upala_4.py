def main():
    text = input()

    if text == text[::-1]:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
