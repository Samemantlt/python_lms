import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, x, y):
        self.x += x
        self.y += y
        
    def length(self, other):
        return f'{math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2):.2f}'
