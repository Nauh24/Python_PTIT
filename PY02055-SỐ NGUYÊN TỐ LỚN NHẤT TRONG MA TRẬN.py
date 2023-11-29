import math


def isPrime(n):
    if n<2: return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0: return False
    return True
n,m=map(int,input().split())
a=[]
Max=0
ok=False
for i in range(n):
    a.append(list(map(int,input().split())))
    for j in range(m):
        if isPrime(a[i][j]) and a[i][j]>Max:
            ok=True
            Max=a[i][j]
if not ok: print('NOT FOUND')
else:
    print(Max)

    for i in range(n):
        for j in range(m):
            if a[i][j]==Max:
                print('Vi tri [{}][{}]'.format(i,j))


'''
6 4
23 21 26 10
13 13 22 14
28 29 28 23
29 19 11 19
16 26 24 21
13 25 21 29
'''