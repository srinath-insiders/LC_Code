def palindromePermutation(s):
    s = s.replace(" ","")
    s = s.lower()
    hm = dict()

    for i in s:
        if i in hm:
            hm[i] += 1
        else:
            hm[i] = 1
    count = 0

    for key, value in hm.items():
        if value % 2 != 0 and count == 0:
            count += 1
        elif value % 2 != 0 and count == 1:
            return False
    return True           



palin_perm = "Tact Coa"
not_palin_perm = "This is not a palindrome permutation"

print(palindromePermutation(palin_perm))
print(palindromePermutation(not_palin_perm))