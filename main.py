class Stack:
    def __init__(self):
        self.values = []

    def is_empty(self):
        return len(self.values) == 0

    def push(self, item):
        self.values.append(item)

    def pop(self):
        return self.values.pop()

    def peek(self):
        return self.values[-1]

    def size(self):
        return len(self.values)