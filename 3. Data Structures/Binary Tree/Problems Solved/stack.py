"""
Stack Data Structure.
"""
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):  
        if not self.is_empty():
            return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items

# myStack = Stack()
# myStack.push("A")
# myStack.push("B")
# myStack.push("C")
# myStack.push("D")
# myStack.pop()

# print(myStack.items)
# myStack.push(myStack.pop())
# print(myStack.items)