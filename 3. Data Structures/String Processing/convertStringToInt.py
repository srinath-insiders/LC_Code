def convert(s):
    if s[0] == "-":
        s = s.replace("-","")
        isNegative = True
    else:
        isNegative = False     
    zeros = len(s) - 1
    result = 0
    for i in s:
        result += (ord(i)-48) * (10 ** zeros)
        zeros -= 1

    if isNegative == True:
        result = result * -1

    print(result)



convert('-276')
