from sys import stdin


def main():
    lines = []
    for line in stdin:
        lines.append(line.rstrip('\n'))
    
    letter_dict = {
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'E',
        'Ж': 'ZH',
        'З': 'Z',
        'И': 'I',
        'Й': 'I',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'KH',
        'Ц': 'TC',
        'Ч': 'CH',
        'Ш': 'SH',
        'Щ': 'SHCH',
        'Ъ': '',
        'Ы': 'Y',
        'Ь': '',
        'Э': 'E',
        'Ю': 'IU',
        'Я': 'IA'
    }
    
    def map_letter(letter):
        if letter in letter_dict:
            return letter_dict[letter]
        else:
            return letter

    with open('cyrillic.txt') as file:
        text = file.read()

    with open('transliteration.txt', 'w') as file:
        for symbol in text:
            up = symbol.isupper()
            result = map_letter(symbol.upper()).lower()
            
            if up and len(result) > 0:
                result = result[0].upper() + result[1:]
            
            file.write(result)


if __name__ == '__main__':
    main()
