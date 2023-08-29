import math
def isPrime(k):
    if k<2:
        return False
    for i in range(2,int(math.sqrt(k))+1):
        if k%i==0: return False
    return True
for t in range(int(input())):
    n=int(input())
    k=0
    for i in range(1,n):
        if math.gcd(i,n)==1:
            k+=1
    if isPrime(k):
        print('YES')
    else:
        print('NO')