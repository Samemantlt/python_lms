class RedButton:
    def __init__(self):
        self.counter = 0
    
    def click(self):
        print('Тревога!')
        self.counter += 1
    
    def count(self):
        return self.counter
