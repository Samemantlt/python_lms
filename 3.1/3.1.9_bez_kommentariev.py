from sys import stdin


def process_line(text):
    if text.startswith('#'):
        return None
    
    index = text.find('#')
    if index == -1:
        return text
    else:
        return text[:index] + '\n'


def main():
    for line in stdin:
        processed = process_line(line)
        if processed is not None:
            print(processed, end='')


if __name__ == '__main__':
    main()
