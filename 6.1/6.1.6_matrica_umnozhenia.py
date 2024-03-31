import numpy


def multiplication_matrix(n):
    line = numpy.arange(1, n + 1)
    print(line)
    print(line.transpose())
    return line * line[:, None]

multiplication_matrix(5)