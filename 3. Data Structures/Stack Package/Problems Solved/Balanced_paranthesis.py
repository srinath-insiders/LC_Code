from Stack import Stack

def check_balanced_paranthesis(val):
    dict = {
        "}":"{",
        ")":"(",
        "]":"["
    }

    stack = Stack()

    for i in range(len(val)):
        if val[i] in dict:
            if stack.pop() != dict[val[i]]:
                return False
        else:
            stack.push(val[i])


    return stack.get_stack() == []

print(check_balanced_paranthesis("(((({}))))"))
print(check_balanced_paranthesis("[][]]]"))
print(check_balanced_paranthesis("[][]"))
print(check_balanced_paranthesis("}"))
print(check_balanced_paranthesis("{"))