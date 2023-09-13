import math

MAX=int(1e6)
prime =[1]*MAX
prime[0]=prime[1]=0
for i in range(2,int(math.sqrt(MAX))):
    if prime[i]:
        for j in range(i*i,MAX,i):
            prime[j]=0

for t in range(int(input())):
    n=int(input())
    used =[]
    for i in range(0,n):
        s=str(i)[::-1]
        if prime[i] and prime[int(s)] and str(i)!=s and int(s)<n and i not in used:
            print(i,s,end=' ')

            used +=[i,int(s)]

    print()