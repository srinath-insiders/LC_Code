class ReverseString:
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

    def reverseString(self, s):
        index = 0
        while index < len(s):
            self.push(s[index])
            index += 1    
   
        reverse_str = ""
        while not self.is_empty():
            reverse_str += self.pop()
        return reverse_str         
          


rs = ReverseString()
print(rs.reverseString('!evitacudE ot emocleW')) 