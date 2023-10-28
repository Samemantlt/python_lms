def main():
    words = [word for _ in range(int(input())) for word in input().split(', ')]

    for i, word in enumerate(sorted(words)):
        print(f'{i + 1}. {word}')


if __name__ == '__main__':
    main()
