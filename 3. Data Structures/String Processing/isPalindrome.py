def is_Palindrome(s):
    s = ''.join([i for i in s if i.isalnum()]).replace(" ","").lower()
    return s == s[::-1]


def is_palindrome_preferrred_solution(s):
    i = 0
    j = len(s) - 1
    s = s.lower()
    while i < j:
        if not s[i].isalnum() and i < j:
            i += 1
        if not s[j].isalnum() and i < j:
            j -= 1

        if s[i] != s[j]:
            return False
        i += 1
        j -= 1    
    return True                


print(is_Palindrome("radar")) 
print(is_palindrome_preferrred_solution("Was it a cat I saw?"))    
print(is_palindrome_preferrred_solution("Never odd or even"))    
