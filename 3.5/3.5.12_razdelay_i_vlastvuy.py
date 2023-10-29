def write_if(text: str, filename: str, predicate):
    lines = text.splitlines()

    with open(filename, 'w') as file:
        for line in lines:
            nums = [i for i in line.split() if predicate(int(i))]
            file.write(' '.join(nums))
            file.write('\n')


def count_odd(num: int):
    c1 = 0

    for symbol in str(num):
        n = int(symbol)
        if n % 2 == 1:
            c1 += 1
    
    return c1


def count_even(num: int):
    c0 = 0

    for symbol in str(num):
        n = int(symbol)
        if n % 2 == 0:
            c0 += 1
    
    return c0


def main():
    filename = input()
    with open(filename) as file:
        text = file.read()

    write_if(text, input(), lambda a: count_even(a) > count_odd(a))
    write_if(text, input(), lambda a: count_even(a) < count_odd(a))
    write_if(text, input(), lambda a: count_even(a) == count_odd(a))


if __name__ == '__main__':
    main()
