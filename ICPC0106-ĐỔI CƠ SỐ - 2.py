from math import log2
f='0123456789ABCDEF'
for t in range(int(input())):
    b=int(input())
    s=input()
    ans=int(log2(int(b)))
    while len(s)%ans!=0:
        s='0'+s
    res=''
    for i in range(0,len(s),ans):
        sum=0
        for j in range(i,i+ans):
            if s[j]=='1':
                sum+=pow(2,ans-(j-i)-1)
        res+=f[sum%16]
    print(res)

