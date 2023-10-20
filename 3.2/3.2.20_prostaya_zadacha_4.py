def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    
    return a


def main():
    nums = set(map(int, input().split('; ')))

    for a in sorted(nums):
        prostie = []

        for b in nums:
            if nod(a, b) == 1:
                prostie.append(b)
        
        if len(prostie) > 0:
            print(f'{a} - {", ".join(map(str, sorted(prostie)))}')


if __name__ == '__main__':
    main()
