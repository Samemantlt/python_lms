import math


class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if a != 0:
        D = b ** 2 - 4 * a * c
        if D < 0:
            raise NoSolutionsError()
        elif D == 0:
            return (-b / (2 * a), -b / (2 * a))
        else:
            roots = [(-b - math.sqrt(D)) / (2 * a), (-b + math.sqrt(D)) / (2 * a)]
            return min(roots), max(roots)
    elif b != 0:
        return (-c / b, -c / b)
    elif c != 0:
        raise NoSolutionsError()
    else:
        raise InfiniteSolutionsError()
