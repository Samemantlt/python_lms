from sys import stdin


def main():
    lines = []
    for line in stdin:
        lines.append(line.rstrip('\n'))
    
    query = lines[-1]
    texts = lines[:-1]

    for text in texts:
        if query.lower() in text.lower():
            print(text)


if __name__ == '__main__':
    main()
