import json
from sys import stdin


def main():
    words = []
    for line in stdin:
        words.append(line.strip())

    result = {}

    for word in sorted(words):
        word = word.lower()
        for index in range(1, len(word), 2):
            letter = word[index]
            if letter not in result:
                result[letter] = []
            
            result[letter].append(word)
    
    for key in result:
        result[key] = sorted(list(set(result[key])))

    with open('result.json', 'w') as file:
        json.dump(result, file)


if __name__ == '__main__':
    main()
