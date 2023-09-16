n=int(input())
a=[[]]*n
for i in range(n):
    a[i]=list(map(int,input().split()))
s1,s2=0,0
for i in range(n):
    for j in range(n):
        if j<n-i-1:
            s1+=a[i][j]
        elif j>n-i-1:
            s2+=a[i][j]
sub=abs(s1-s2)
k=int(input())
if sub<=k:
    print('YES')
else:
    print('NO')
print(sub)
