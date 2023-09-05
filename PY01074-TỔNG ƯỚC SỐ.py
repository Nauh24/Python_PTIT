import math
x=2000000
prime =[0]*x
def snt():
    global x
    for i in range(2,int(math.sqrt(x))+1):
        if prime[i]==0:
            for j in range(i,x+1):
                prime[j]=i
    for i in range(2,x+1):
        prime[i]=i

res=0
snt()
def nto(n):
    sum=0
    while n!=1:
        sum+=prime[n]
        n//=prime[n]

    return sum
for t in range(int(input())):
    n=int(input())
    res+=nto(n)
print(int(res))