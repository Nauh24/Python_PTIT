import math
def snt(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0 : return False
    return True
for t in range(int(input())):
    a,b=map(int,input().split())
    c=math.gcd(a,b)
    s=sum(int(i) for i in str(c))
    if snt(s): print('YES')
    else : print('NO')
    print()
