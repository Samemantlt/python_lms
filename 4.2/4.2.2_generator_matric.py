def make_matrix(size, value=0):
    if isinstance(size, int):
        size = (size, size)

    arr = []
    for x in range(size[1]):
        arr.append([value] * size[0])
    
    return arr


if __name__ == '__main__':
    main()
