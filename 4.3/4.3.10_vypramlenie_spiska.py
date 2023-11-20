from collections.abc import Iterable


def make_linear(*args):
    output = []

    for arg in args:
        if isinstance(arg, Iterable):
            output += make_linear(arg)
        else:
            output.append(arg)
    
    return output
