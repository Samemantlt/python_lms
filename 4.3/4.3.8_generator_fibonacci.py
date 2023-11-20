def fibonacci(n):
    if n <= 0:
        return

    a = 0
    b = 1

    if n >= 1:
        yield a
        
        if n >= 2:
            yield b

    for i in range(n - 2):
        c = a + b
        a = b
        b = c
        yield c
