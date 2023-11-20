def merge(a: tuple, b: tuple):
    arr = []

    a_it = iter(a)
    b_it = iter(b)

    a_last = next(a_it, None)
    b_last = next(b_it, None)

    while a_last is not None or b_last is not None:
        if a_last is None:
            arr.append(b_last)
            b_last = next(b_it, None)
            continue

        if b_last is None:
            arr.append(a_last)
            a_last = next(a_it, None)
            continue

        if a_last > b_last:
            arr.append(b_last)
            b_last = next(b_it, None)
            continue

        arr.append(a_last)
        a_last = next(a_it, None)
        continue
    
    return tuple(arr)


if __name__ == '__main__':
    assert merge((1, 5), (2, 4)) == (1, 2, 4, 5)
    assert merge((1, 3), (2, 4)) == (1, 2, 3, 4)
    assert merge((1, 3), (2, 4, 4)) == (1, 2, 3, 4, 4)
