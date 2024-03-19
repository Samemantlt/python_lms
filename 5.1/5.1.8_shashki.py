def parse_address(address: str):
    x_str = address[0]
    y_str = address[1]

    x = 'ABCDEFGH'.index(x_str)
    y = '12345678'.index(y_str)

    return x, y


def create_default_world():
    world = [['X' for _ in range(8)] for _ in range(8)]

    for i in range(0, 8, 2):
        world[i][0] = 'W'
        world[i][2] = 'W'

        world[i][6] = 'B'

    for i in range(1, 8, 2):
        world[i][1] = 'W'

        world[i][5] = 'B'
        world[i][7] = 'B'
    
    return world


class Cell:
    def __init__(self, value):
        self.value = value

    def status(self):
        return self.value


class Checkers:
    def __init__(self):
        self.world = create_default_world()

    def get_cell(self, address: str):
        address = parse_address(address)
        value = self.world[address[0]][address[1]]
        return Cell(value)
    
    def move(self, fromAddress: str, toAddress: str):
        fromAddress = parse_address(fromAddress)
        toAddress = parse_address(toAddress)
        
        oldVal = self.world[fromAddress[0]][fromAddress[1]]
        for x in range(fromAddress[0], toAddress[0], 1 if fromAddress[0] < toAddress[0] else -1):
            for y in range(fromAddress[1], toAddress[1], 1 if fromAddress[1] < toAddress[1] else -1):
                self.world[x][y] = 'X'
        
        self.world[toAddress[0]][toAddress[1]] = oldVal
