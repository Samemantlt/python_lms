def main():
    nums = []

    for _ in range(int(input())):
        nums.append(int(input()))
    
    power = int(input())

    for num in nums:
        print(num ** power)


if __name__ == '__main__':
    main()
