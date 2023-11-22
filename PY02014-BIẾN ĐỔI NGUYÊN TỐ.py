import math


def snt(n):
    if n<2:
        return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return True
n=int(input())
a=[]
while len(a)<n:
    a+=list(map(int,input().split()))

min_step=0
for i in a:
    j=0
    k=0
    while not snt(i+j):
        j+=1
    while not snt(i-k):
        k+=1
    min_step=max(min_step,min(j,k))
print(min_step)



'''
8
13 5 8 7 9 15 26 34
'''