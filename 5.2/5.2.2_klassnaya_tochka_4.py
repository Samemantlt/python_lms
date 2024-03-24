import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, x, y):
        self.x += x
        self.y += y
        
    def length(self, other):
        return f'{round(math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2), 2)}'


class PatchedPoint(Point):
    def __init__(self, x=0, y=0):
        if isinstance(x, tuple):
            x, y = x
        super().__init__(x, y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'PatchedPoint({self.x}, {self.y})'
