class Queue:
    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)
    
    def pop(self):
        return self.array.pop(0)
    
    def is_empty(self):
        return len(self.array) == 0
