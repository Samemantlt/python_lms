def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    
    return a


def main():
    count = int(input()) - 1

    result = int(input())
    
    for _ in range(count):
        b = int(input())
        result = nod(result, b)
    
    print(result)


if __name__ == '__main__':
    main()
