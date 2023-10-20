def preprocess_str(text: str):
    result = ''
    for symbol in text:
        if symbol == ' ':
            continue

        result += symbol.lower()
    
    return result


def main():
    text = input()
    text = preprocess_str(text)

    if text == text[::-1]:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
