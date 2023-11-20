def recursive_sum(*args):
    if len(args) == 1:
        return args[0]
    else:
        return args[0] + recursive_sum(*args[1:])
