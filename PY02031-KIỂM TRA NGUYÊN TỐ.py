import math


def isPrime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True
n,m=map(int,input().split())
for i in range(n):
    a=list(map(int,input().split()))
    for j in a:
        if isPrime(j):
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()