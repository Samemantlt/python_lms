def main():
    nums = [int(x) for x in input().split(' ')]
    power = int(input())
    
    print(' '.join([str(num ** power) for num in nums]))


if __name__ == '__main__':
    main()
