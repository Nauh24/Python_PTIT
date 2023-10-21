import math
from sys import stdin

for t in range(int(input())):
    n,k=map(int,input().split())

    a=[]
    cnt=0
    for line in stdin :
        a+=list(map(int,line.split()))
        if len(a)==n: break


    minn=10**10;
    for i in range(n):
        res =a[i];
        len=0
        for j in range(i,n):
            res=math.gcd(a[j],res)
            if res==k:
                len=j-i+1
                minn=min(len,minn)
                break
    if minn==10**10:
        print(-1)
    else:
        print(minn)
    a.clear()
'''
3
8 3
6 9 7 10 12 24 36 27
4 3
2 4 6 8
4 6
1 2 3 6
'''