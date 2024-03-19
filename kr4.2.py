numbers = []


def add_number(number):
    numbers.append(number)


def get_sum():
    return ' + '.join([str(number) for number in numbers]) + ' = ' + sum(numbers)
