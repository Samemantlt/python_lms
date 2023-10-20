import math


def main():
    number = int(input())
    
    if number <= 1:
        print('NO')
        exit()
    
    for i in range(2, number):
        if number % i == 0:
            print('NO')
            exit()
    
    print('YES')
    exit()


if __name__ == '__main__':
    main()
