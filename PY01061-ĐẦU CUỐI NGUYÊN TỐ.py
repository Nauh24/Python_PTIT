import math


def snt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
for t in range(int(input())):
    s=input()
    dau=int(s[0:3])
    cuoi=int(s[-3:])
    if snt(dau) and snt(cuoi):
        print('YES')
    else:
        print('NO')