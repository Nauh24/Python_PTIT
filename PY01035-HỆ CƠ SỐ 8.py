def trans(s):
    tong=0
    b=2
    for i in s:
        tong+=int(i)*2**b
        b-=1
    return tong
s=input()
while len(s)%3!=0:
    s='0'+s
a=list(s[i:i+3] for i in range(0,len(s),3))
ans=''
for i in a:
    ans+=str(trans(i))
print(ans)