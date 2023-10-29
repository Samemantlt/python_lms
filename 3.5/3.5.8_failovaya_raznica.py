def main():
    filename = input()
    with open(filename) as file:
        text1 = file.read()

    filename = input()
    with open(filename) as file:
        text2 = file.read()
    
    filename = input()

    words1 = set(text1.split())
    words2 = set(text2.split())

    result = []

    for word in words1.symmetric_difference(words2):
        result.append(word)
    
    with open(filename, 'w') as file:
        for word in sorted(result):
            file.write(word + '\n')


if __name__ == '__main__':
    main()
