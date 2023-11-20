already_printed = set()


def modern_print(text: str):
    if text not in already_printed:
        already_printed.add(text)
        print(text)


if __name__ == '__main__':
    main()
