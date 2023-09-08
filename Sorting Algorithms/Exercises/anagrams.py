def comp(s1, s2):
    res = 0
    for i in range(len(s1)):
        res += ord(s1[i])**2
        res -= ord(s2[i])**2
    
    return res == 0

print(comp("aba", "aab"))