import math


def isPrime(n):
    if n<2:
        return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return True

n=int(input())
a=list(map(int,input().split()))
d={}
b=[]
for i in range(n):
    if a[i] not in b:
        b.append(a[i])
    else: continue
Sum=sum(b)
ok=False

for i in range(len(b)):
    if isPrime(sum(b[:i+1])) and isPrime(sum(b[i+1:])):
        print(i)
        ok=True
        break
if not ok:
    print('NOT FOUND')




'''
10
3 6 7 3 4 7 3 6 4 4

10
3 6 7 3 5 7 3 6 6 7
'''