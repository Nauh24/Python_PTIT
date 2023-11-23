import math


def isPrime(n):
    if n<2: return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0: return False
    return True
n=int(input())
a=list(map(int,input().split()))
idx=0
b=[]
for i in a:
    if isPrime(i):
        b.append(i)
b=sorted(b)
#print(*b)
for i in a:
    if isPrime(i):
        print(b[idx],end=' ')
        idx+=1
    else:
        print(i,end=' ')
'''
8
4 6 3 8 7 2 5 9
'''