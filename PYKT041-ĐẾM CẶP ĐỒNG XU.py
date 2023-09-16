from math import comb

n=int(input())
a=[]
for i in range(n):
    a.append(list(input()))
cnt=0
dem=0
for i in range(n):
    cnt=a[i].count('C')
    dem += comb(cnt, 2)
for j in range(n):
    cnt=0
    for i in range(n):
        if a[i][j]=='C':
            cnt+=1
    dem+=comb(cnt,2)
print(dem)


