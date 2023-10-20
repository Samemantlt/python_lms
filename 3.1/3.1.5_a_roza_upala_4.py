def main():
    text = input()

    if text == ''.join(reversed(text)):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
