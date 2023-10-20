def main():
    n = int(input())

    objects = set()
    for _ in range(n):
        text = input()
        words = text.split(' ')
        for word in words:
            objects.add(word)
    
    for word in objects:
        print(word)


if __name__ == '__main__':
    main()
