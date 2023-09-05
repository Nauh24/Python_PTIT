def check(s):
    if len(s)<3: return 'no'
    s=s.lower()
    if s[-3:] != '.py':
        return 'no'
    for i in range(0,len(s)-3):
        if not s[i].isalpha() and s[i]!='.' and s[i]!='_':
            return 'no'
    return 'yes'
s=input()
print(check(s))
