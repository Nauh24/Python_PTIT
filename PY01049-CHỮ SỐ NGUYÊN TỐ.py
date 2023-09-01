import math


def snt(n):
    if n<2 :
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True
def check(s):
    cnt=0
    for i in range(len(s)):
        if snt(int(s[i]))==True: cnt+=1;
    return cnt>len(s)-cnt
for t in range(int(input())):
    s=input()
    l =len(s)
    if snt(l) and check(s):
        print('YES')
    else:
        print('NO')
