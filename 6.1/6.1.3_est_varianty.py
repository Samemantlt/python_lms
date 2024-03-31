from math import comb


guests, places = map(int, input().split())

print(comb(guests - 1, places - 1), end=" ")
print(comb(guests, places))