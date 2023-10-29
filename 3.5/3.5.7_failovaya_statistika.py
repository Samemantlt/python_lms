def avg(seq):
    return sum(seq) / len(seq)


def main():
    filename = input()

    with open(filename) as file:
        text = file.read()
    
    nums = [int(i) for i in text.split()]

    print(len(nums))
    print(len([i for i in nums if i > 0]))
    print(min(nums))
    print(max(nums))
    print(sum(nums))
    print(f'{avg(nums):.2f}')


if __name__ == '__main__':
    main()
