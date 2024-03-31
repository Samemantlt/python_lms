nums = [float(i) for i in input().split()]

cnt = 0
mul = 1
for num in nums:
    cnt += 1
    mul *= num

print(mul ** (1 / cnt))