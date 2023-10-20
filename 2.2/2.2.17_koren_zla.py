import math


def main():
    a = float(input())
    b = float(input())
    c = float(input())

    if a != 0:
        D = b ** 2 - 4 * a * c
        if D < 0:
            print('No solution')
        elif D == 0:
            print(f'{-b / (2 * a):2f}')
        else:
            roots = [(-b - math.sqrt(D)) / (2 * a), (-b + math.sqrt(D)) / (2 * a)]
            print(f'{min(roots):.2f}', end=" ")
            print(f'{max(roots):.2f}')
    elif b != 0:
        print(f'{-c / b:.2f}')
    elif c != 0:
        print('No solution')
    else:
        print('Infinite solutions')


if __name__ == '__main__':
    main()
