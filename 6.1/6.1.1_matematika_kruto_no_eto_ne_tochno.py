import math


x = float(input())

result = math.log(x ** (3 / 16), 32) + x ** math.cos(math.pi * x / (2 * math.e)) - math.sin(x / math.pi) ** 2

print(result)