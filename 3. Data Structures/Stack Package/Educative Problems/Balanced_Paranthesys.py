class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return self.items == [] 

    def get_stack(self):
        return self.items

    def balanced_paranthesis(self, input):
        dict = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        self.items = []
        for i in range(len(input)):
            if input[i] not in dict:
                self.push(input[i])
            else:
                if dict[input[i]] == self.peek():
                    self.pop()
                else:
                    return False

        return self.is_empty()            


myStack = Stack()
print(myStack.balanced_paranthesis("({})"))
print(myStack.balanced_paranthesis("(((({)})))"))
print(myStack.balanced_paranthesis("[][]]]"))
print(myStack.balanced_paranthesis("[][]"))

