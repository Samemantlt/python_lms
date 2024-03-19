def grasshopper_inner(start, finish, length):
    if start == finish:
        if length == 0:
            return [[finish]]
        else:
            return []

    if length == 0:
        return []

    anothers = [
        *grasshopper_inner(start + 1, finish, length - 1),
        *grasshopper_inner(start + 2, finish, length - 1),
        *grasshopper_inner(start - 1, finish, length - 1),
        *grasshopper_inner(start - 2, finish, length - 1),
    ]

    result = []
    for i in anothers:
        if i is not None:
            result.append([start] + list(i))
    
    return result


def grasshopper(*args):
    return grasshopper_inner(*args)
