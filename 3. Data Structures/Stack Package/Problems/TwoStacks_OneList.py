class TwoStacks:
    def __init__(self, size):
        self.size = size
        self.arr = [0]*size
        self.top1 = 0
        self.top2 = size-1


    def push1(self, val):
        if self.top1 <= self.top2:
            self.arr[self.top1] = val
            self.top1 += 1
        else:
            print("stack overflow")

    def push2(self, val):
        if self.top1 <= self.top2:
            self.arr[self.top2] = val
            self.top2 -= 1
        else:
            print("stack overflow")

    def pop1(self):
        if self.top1 > 0:
            self.top1 = self.top1 - 1
            val = self.arr[self.top1]
            self.arr[self.top1] = 0
            return val
        else:
            print("stack underflow") 

    def pop2(self):
        if self.top2 < self.size-1:
            self.top2 = self.top2 + 1
            val = self.arr[self.top2]
            self.arr[self.top2] = 0 
            return val
        else:
            print("stack underflow") 
                    

stack = TwoStacks(3)
stack.push1(1)
stack.push1(5)
stack.push2(3)
stack.push2(2)
print(stack.arr)