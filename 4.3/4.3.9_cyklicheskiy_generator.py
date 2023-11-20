# Copied from https://docs.python.org/3/library/itertools.html#itertools.cycle
def cycle(iter):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    
    while saved:
        for element in saved:
              yield element


if __name__ == '__main__':
    main()
