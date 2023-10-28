def main():
    words = input().split()

    for i in range(len(words)):
        print(' '.join(words[:i + 1]))


if __name__ == '__main__':
    main()
