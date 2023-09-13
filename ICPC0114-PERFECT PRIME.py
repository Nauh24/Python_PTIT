import math


def isPrime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True
def tong(n):
    for i in n:
        if not isPrime(int(i)): return False
    s=sum([int(i) for i in n])
    if isPrime(s):
        return True
    else: return False


for t in range(int(input())):
    n=int(input())
    n2=str(n)[::-1]
    if isPrime(n) and isPrime(int(n2)) and tong(str(n)) :
        print('Yes')
    else:
        print('No')
