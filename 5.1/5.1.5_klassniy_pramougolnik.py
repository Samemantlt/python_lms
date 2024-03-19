class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def sides(self):
        width = abs(self.a[0] - self.b[0])
        height = abs(self.a[1] - self.b[1])

        return round(width, 2), round(height, 2)

    def area(self):
        width, height = self.sides()
        return round(width * height, 2)
    
    def perimeter(self):
        width, height = self.sides()
        return round(2 * (width + height), 2)
