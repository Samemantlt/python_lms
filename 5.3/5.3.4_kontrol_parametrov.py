def only_positive_even_sum(a, b):
    if type(a) is not int or type(b) is not int:
        raise TypeError()
    if a < 0 or a % 2 == 1:
        raise ValueError()
    if b < 0 or b % 2 == 1:
        raise ValueError()
    return a + b