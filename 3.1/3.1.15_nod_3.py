def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    
    return a


def main():
    nums = [int(x) for x in input().split(' ')]
    
    result = nod(nums[0], nums[1])
    for i in range(2, len(nums)):
        result = nod(result, nums[i])
    
    print(result)


if __name__ == '__main__':
    main()
