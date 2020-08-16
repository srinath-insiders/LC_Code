
class Solution:
    
    def __init__(self):
        self.stack = []
        self.parans = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        self.openingBrackets = '({['
        self.closingBrackets = ')}]'

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

    def isEmpty(self):
        return self.stack == []    

    def isValid(self, s):
        for item in s:
            if item in self.openingBrackets:
                self.push(item)
            elif item in self.closingBrackets:
                if not self.isEmpty():
                    if self.parans.get(item) != self.pop():
                        return False    
                else:
                    return False
            else:
                return False

        if len(s) == 0:
            return False        
        else:
            return not self.stack

s = Solution()
print(s.isValid(")"))
