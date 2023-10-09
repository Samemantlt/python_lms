def main():
    max_length = int(input())

    for _ in range(int(input())):
        text = input()
        if len(text) > max_length:
            print(f'{text[:max_length - 3]}...')
        else:
            print(text)


if __name__ == '__main__':
    main()
