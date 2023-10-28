def to_num(val):
    return 1 if val else 0


def main():
    values = [False, True]
    expression = input()
    
    print('a b c f')
    for a in values:
        for b in values:
            for c in values:
                f = eval(expression, None, {'a': a, 'b': b, 'c': c})

                print(f'{to_num(a)} {to_num(b)} {to_num(c)} {to_num(f)}')


if __name__ == '__main__':
    main()
