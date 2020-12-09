class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def is_empty(self):
        return self.items == []

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items





