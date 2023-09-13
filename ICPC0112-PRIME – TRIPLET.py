import math
MAX =int(1e6+1)
prime=[1]*MAX
prime[0]=prime[1]=0
for i in range(int(math.sqrt(MAX))):
    if prime[i]:
        for j in range(i*i,MAX,i):
            prime[j]=0


for t in range (int(input())):
    n=int(input())
    cnt=0
    for i in range(5,n-6):
        if prime[i] and prime[i+6]:
            if prime[i+2] or prime[i+4]:
                cnt+=1
    print(cnt)

