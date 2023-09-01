def check(s):
    for i in range(2,len(s),2):
        if s[i]!=s[i-2]:
            return False
    return True
for t in range(int(input())):
    s=input()
    l=len(s)
    if l%2==1 and s[0]!=s[1] and check(s):
        print('YES')
    else:
        print('NO')
