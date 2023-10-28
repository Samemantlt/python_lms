import itertools


def to_num(val):
    return 1 if val else 0


def main():
    values = [False, True]
    expression = input()

    variables = sorted(list({letter for letter in expression if letter.isupper()}))
    
    print(' '.join(variables + ['F']))

    for current_values in itertools.product(values, repeat=len(variables)):
        local_variables = {variables[i]: current_values[i] for i in range(len(variables))}
        f = eval(expression, None, local_variables)

        print(' '.join([str(to_num(i)) for i in list(current_values) + [f]]))


if __name__ == '__main__':
    main()
