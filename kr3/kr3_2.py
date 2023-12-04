def main():
    word_map = {}

    while (line := input()) != '':
        words = line.split()
        
        for word in words:
            letter = word[(len(word) + 1) // 2 - 1].upper()
            if letter not in word_map:
                word_map[letter] = set()
            word_map[letter].add(word.lower())

    for letter, words in word_map.items():
        print(f'{letter.lower()} "{". ".join(map(str.upper, sorted(list(words))))}"')


if __name__ == '__main__':
    main()
