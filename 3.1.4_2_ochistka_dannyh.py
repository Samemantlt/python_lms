import sys


def main():
    for text in sys.stdin:
        text = text[:-1] if text.endswith('\n') else text

        if not text.endswith('@@@'):
            if text.startswith('##'):
                print(text[2:])
            else:
                print(text)


if __name__ == '__main__':
    main()
