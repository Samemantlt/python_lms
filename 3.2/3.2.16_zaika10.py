def main():
    lines = []
    near = set()

    while (line := input()) != '':
        lines.append(line)
    
    for line in lines:
        words = line.split(' ')

        for i, word in enumerate(words):
            if word == 'зайка':
                if i > 0:
                    near.add(words[i - 1])
                if i < len(words) - 1:
                    near.add(words[i + 1])
    
    for word in near:
        print(word)


if __name__ == '__main__':
    main()
