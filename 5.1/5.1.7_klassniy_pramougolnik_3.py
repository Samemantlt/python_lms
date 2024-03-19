def avg(*args):
    return sum(args) / len(args)


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_size(self):
        width = abs(self.a[0] - self.b[0])
        height = abs(self.a[1] - self.b[1])

        return round(width, 2), round(height, 2)

    def move(self, dx, dy):
        self.a = (self.a[0] + dx, self.a[1] + dy)
        self.b = (self.b[0] + dx, self.b[1] + dy)

    def get_pos(self):
        return min(self.a[0], self.b[0]), max(self.a[1], self.b[1])

    def area(self):
        width, height = self.get_size()
        return width * height
    
    def perimeter(self):
        width, height = self.get_size()
        return round(2 * (width + height), 2)

    def resize(self, width, height):
        pos = self.get_pos()
        a = pos
        b = (pos[0] + width, pos[1] - height)

    def center(self):
        x = avg(self.a[0], self.b[0])
        y = avg(self.a[1], self.b[1])

        return x, y
    
    def turn(self):
        x, y = self.center()
        width, height = self.get_size()

        a = (x - height / 2, y - width / 2)
        b = (x + height / 2, y + width / 2)

        self.a = a
        self.b = b

    def scale(self, factor):
        x, y = self.center()
        width, height = self.get_size()

        a = (x - (width / 2) * factor, y - (height / 2) * factor)
        b = (x + (width / 2) * factor, y + (height / 2) * factor)

        self.a = a
        self.b = b
