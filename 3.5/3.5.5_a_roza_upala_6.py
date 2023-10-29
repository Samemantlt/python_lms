from sys import stdin


def main():
    lines = []
    for line in stdin:
        lines.append(line.rstrip('\n'))
    
    words = []
    for line in lines:
        words += line.split()

    result = set()

    for word in words:
        compare_word = word.lower()
        if compare_word == compare_word[::-1]:
            result.add(word)
    
    for word in sorted(result):
        print(word)


if __name__ == '__main__':
    main()
