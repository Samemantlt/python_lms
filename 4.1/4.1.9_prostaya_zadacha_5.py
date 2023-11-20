import math


def is_prime(num: int):
    for i in range(2, math.ceil(math.sqrt(num))):
        if num % i == 0:
            return False
    
    return True


if __name__ == '__main__':
    main()
