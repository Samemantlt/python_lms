def is_prostoe(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True


def main():
    count = int(input())
    result = 0

    for _ in range(count):
        num = int(input())
        if is_prostoe(num):
            result += 1
    
    print(result)


if __name__ == '__main__':
    main()
