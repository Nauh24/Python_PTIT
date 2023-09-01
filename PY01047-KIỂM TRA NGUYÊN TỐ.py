import math


def snt(s):
    if s<2: return False
    for i in range(2,int(math.sqrt(s))+1):
        if s%i==0 : return False
    return True
for t in range(int(input())):
    s=input()

    s=s[-4:]
    if snt(int(s)): print('YES')
    else: print('NO')