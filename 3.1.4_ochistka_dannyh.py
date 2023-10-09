import sys


def main():
    for text in sys.stdin:
        if text.startswith('##'):
            print(text[2:])
        elif text.endswith('@@@'):
            pass
        else:
            print(text)


if __name__ == '__main__':
    main()
