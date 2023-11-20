def merge_sort(array):
    if len(array) <= 1:
        return array
    
    right = merge_sort(array[:len(array) // 2])
    left = merge_sort(array[len(array) // 2:])

    r_iter = iter(right)
    l_iter = iter(left)

    r_value = next(r_iter, None)
    l_value = next(l_iter, None)

    result = []
    while len(result) < len(array):
        if r_value is None:
            result.append(l_value)
            l_value = next(l_iter, None)
            continue

        if l_value is None:
            result.append(r_value)
            r_value = next(r_iter, None)
            continue

        if l_value < r_value:
            result.append(l_value)
            l_value = next(l_iter, None)
            continue
        else:
            result.append(r_value)
            r_value = next(r_iter, None)
            continue
    
    return result


if __name__ == '__main__':
    assert merge_sort([4, 1, 3, 1, 2, 7, 5]) == [1, 1, 2, 3, 4, 5, 7]