import math


x1, y1 = map(float, input().split())

p2, f2 = map(float, input().split())

sin = math.sin(f2)
cos = math.cos(f2)

x2 = p2 * cos
y2 = p2 * sin

result = math.dist((x1, y1), (x2, y2))

print(result)