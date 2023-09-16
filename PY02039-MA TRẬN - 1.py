n=int(input())
a =[[]]*n
for i in range(n):
    a[i]=list(map(int,input().split()))
s1 ,s2 =0,0
for i in range(n):
    for j in range(n):
        if i<j:
            s1+=a[i][j]
        elif i>j:
            s2+=a[i][j]

k=int(input())
sub =abs(s1-s2)
if sub<=k:
    print('YES')
else:
    print('NO')
print(sub)