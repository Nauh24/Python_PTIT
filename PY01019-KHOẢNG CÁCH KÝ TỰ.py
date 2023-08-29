def check(a,b):
    for i in range(1,len(a)):
        if abs(ord(a[i])-ord(a[i-1]))!=abs(ord(b[i])-ord(b[i-1])):
            return False
    return True
for t in range(int(input())):
    s1=input()
    s2=s1[::-1]
    if check(s1,s2): print('YES')
    else: print('NO')
