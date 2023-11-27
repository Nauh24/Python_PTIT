import math


def isPrime(n):
    if n<2: return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return True
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
Sum=sum(b)
tong=0
ok=False
for i in range(len(b)):
    tong+=b[i]
    if isPrime(tong) and isPrime(Sum-tong):
        print(i)
        ok=True
        break
if not ok: print('NOT FOUND')

'''
10
3 6 7 3 4 7 3 6 4 4
'''