
s=input()
s=s[::-1]
ans=''
cnt=0
for i in s:
    if cnt==3:
        ans+=','
        cnt=0
    ans+=i
    cnt+=1

ans=ans[::-1]
print(ans)
print()