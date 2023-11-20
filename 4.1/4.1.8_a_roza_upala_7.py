def is_palindrome(obj: int | str | tuple | list):
    if isinstance(obj, int):
        return str(obj) == str(obj)[::-1]
    
    if isinstance(obj, str):
        return obj == obj[::-1]
    
    if isinstance(obj, tuple):
        return obj == tuple(reversed(obj))

    if isinstance(obj, list):
        return obj == list(reversed(obj))
    
    raise Exception('Unknown type')


if __name__ == '__main__':
    main()
