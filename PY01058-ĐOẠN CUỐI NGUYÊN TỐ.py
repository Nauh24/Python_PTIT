import math


def snt(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True
for t in range(int(input())):
    s=input()
    res=int(s[-4:])
    if snt(res):
        print('YES')
    else:
        print('NO')