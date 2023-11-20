import math


nums = []


def enter_results(*values):
    global nums
    nums += values


def _get_sum():
    sum0 = 0
    sum1 = 0

    for i in range(0, len(nums), 2):
        sum0 += nums[i]
    
    for i in range(1, len(nums), 2):
        sum1 += nums[i]

    return sum0, sum1


def get_sum():
    return _get_sum()


def get_average():
    sum0, sum1 = _get_sum()

    avg0 = round(sum0 / (len(nums) / 2), 2)
    avg1 = round(sum1 / (len(nums) / 2), 2)

    return avg0, avg1


if __name__ == '__main__':
    main()
