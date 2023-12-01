n=int(input())+1
a=list(map(int,input().split()))
a.append(-1)
k=max(a)
cnt=0
res=1
for i in range(n):
    if a[i]==k:
        cnt+=1
    else:
        res=max(res,cnt)
        cnt=0
print(res)