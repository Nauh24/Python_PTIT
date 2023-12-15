import math
def isPrime(n):
    if n<2: return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0: return False
    return True
def check(n):
    Sum=0
    while n>0:
        Sum+=n%10
        n//=10
    if isPrime(Sum): return True
    else : return False
    #return Sum
for t in range(int(input())):
    a,b=map(int,input().split())
    c=math.gcd(a,b)
    #print(gcd)
    #print(check(c))
    if check(c): print('YES')
    else: print('NO')

'''
3
28 42
123 18
550 55
'''