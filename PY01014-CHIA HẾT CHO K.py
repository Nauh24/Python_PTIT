
a,k,n=map(int,input().split())
ok=0
st=k-(a%k)+a
for i in range(st,n+1,k):
        ok=1
        print(i-a,end=' ')

if ok==0: print(-1)
print()