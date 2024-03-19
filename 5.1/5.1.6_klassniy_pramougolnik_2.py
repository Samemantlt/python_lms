class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_size(self):
        width = abs(self.a[0] - self.b[0])
        height = abs(self.a[1] - self.b[1])

        return round(width, 2), round(height, 2)

    def move(self, dx, dy):
        self.a = (round(self.a[0] + dx, 2), round(self.a[1] + dy, 2))
        self.b = (round(self.b[0] + dx, 2), round(self.b[1] + dy, 2))

    def get_pos(self):
        return min(self.a[0], self.b[0]), max(self.a[1], self.b[1])

    def area(self):
        width, height = self.sides()
        return width * height
    
    def perimeter(self):
        width, height = self.sides()
        return round(2 * (width + height), 2)

    def resize(self, width, height):
        pos = self.get_pos()
        a = pos
        b = (pos[0] + width, pos[1] - height)
