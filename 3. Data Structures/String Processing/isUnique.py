def is_unique(input_str):
    return len(set(input_str)) == len(input_str)

def is_unique_3(input_str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True

print(is_unique("bhbwjbwjbwdbwd"))   

print(is_unique_3("bhbwjbwjbwdbwd"))    