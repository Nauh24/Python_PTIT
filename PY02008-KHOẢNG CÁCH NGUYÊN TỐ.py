import math

f=[1]*10001
f[0]=f[1]=0
for i in range(2,int(math.sqrt(10001))+1):
    if f[i]==1:
        for j in range(i*i,10001,i):
            f[j]=0
a=[]
for i in range(10001):
    if f[i]==1:
        a.append(i)

n,x=map(int,input().split())
i=0
while i<n+1:
    print(x,end=' ')
    x+=a[i]
    i+=1
