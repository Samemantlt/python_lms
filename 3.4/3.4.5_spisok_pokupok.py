def main():
    words = [
        *input().split(', '),
        *input().split(', '),
        *input().split(', ')
    ]

    for i, word in enumerate(sorted(words)):
        print(f'{i + 1}. {word}')


if __name__ == '__main__':
    main()
