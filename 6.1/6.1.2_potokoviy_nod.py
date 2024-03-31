from math import gcd
import sys

lines = sys.stdin.read().splitlines()

for line in lines:
    if line == '':
        continue

    nums = [int(i) for i in line.split(' ')]
    result = nums[0]
    for i in nums:
        result = gcd(result, i)
    
    print(result)
