import math


def snt(n):
    if n<2 :
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True
def check(s):
    tong=0
    for i in range(0,len(s)):
        if i%2==0 and int(s[i])%2==1:
            return 'NO'
        if i%2==1 and int(s[i])%2==0:
            return 'NO'
        tong+=int(s[i])
    if snt(tong): return 'YES'
    return 'NO'
for t in range(int(input())):
    s=input()
    print(check(s))
