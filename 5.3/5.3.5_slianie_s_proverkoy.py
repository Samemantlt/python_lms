from collections.abc import Iterable


def check_tuple(t: tuple):
    if not isinstance(t, Iterable):
        raise StopIteration()
    
    types = {type(i) for i in t}
    if len(types) > 1:
        raise TypeError()
    
    last = None
    for element in t:
        if last is None:
            last = element
        
        if element < last:
            raise ValueError()


def merge(a: tuple, b: tuple):
    check_tuple(a)
    check_tuple(b)  

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