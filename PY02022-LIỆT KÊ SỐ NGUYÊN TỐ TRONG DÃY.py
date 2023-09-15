import math


def isPrime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
a=list(map(int,input().split()))
d={}

for i in a:
    if i in d:
        d[i]+=1
    else : d[i]=1
for i in d:
   if isPrime(i):
       print(i,d[i],end=' ')
       print()
