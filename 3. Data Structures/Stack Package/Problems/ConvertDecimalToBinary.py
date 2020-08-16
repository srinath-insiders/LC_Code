class ConvertDecimal:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items

    def decimal_to_binary(self, dec_num):
        while dec_num != 0:
            self.push(dec_num % 2)
            dec_num = dec_num // 2
           
        binary_str = ""
        while not self.is_empty():
            binary_str += str(self.pop())
        return binary_str

c = ConvertDecimal()
print(c.decimal_to_binary(56))        