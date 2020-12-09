from Stack import Stack

def convert_int_to_bin(dec_num):
    stack = Stack()
    while (dec_num >= 1):
        stack.push(dec_num % 2)
        dec_num = dec_num // 2

    binaryStr = ""

    while not stack.is_empty():
        binaryStr += str(stack.pop())      

    return binaryStr    

print(convert_int_to_bin(55))
