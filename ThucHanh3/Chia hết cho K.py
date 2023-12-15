a,k,n=map(int,input().split())
ok=False
st=a+k-(a%k)
for i in range(st,n+1,k):
        ok=True
        print(i-a,end=' ')
if not ok:
    print(-1)
print()