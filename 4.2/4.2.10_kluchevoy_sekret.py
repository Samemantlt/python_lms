def secret_replace(text: str, **kwargs):
    for key, values in kwargs.items():
        index = 0
        while key in text:
            text = text.replace(key, values[index % len(values)], 1)
            index += 1

    return text


if __name__ == '__main__':
    main()
