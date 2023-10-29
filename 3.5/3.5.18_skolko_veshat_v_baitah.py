from os.path import getsize
import math


def main():
    filename = input()

    suffixes = ['Б', 'КБ', 'МБ', 'ГБ']
    size = getsize(filename)

    suffix_index = 0
    while size > 1024 and suffix_index + 1 < len(suffixes):
        size = math.ceil(size / 1024)
        suffix_index += 1
    
    print(f'{size}{suffixes[suffix_index]}')


if __name__ == '__main__':
    main()
