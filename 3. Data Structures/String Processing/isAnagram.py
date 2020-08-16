def isAnagram(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

    hm = dict()

    for s in s1:
        if s in hm:
            hm[s] += 1
        else:
            hm[s] = 1

    for s in s2:
        if s in hm:
            hm[s] -= 1
        else:
            hm[s] = 1

    for i in hm:
        if hm[i] != 0:
            return False
    return True                
                   

s1 = "fairy tales"
s2 = "rail safety"

print(isAnagram(s1,s2))