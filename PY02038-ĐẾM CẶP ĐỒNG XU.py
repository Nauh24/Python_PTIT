from math import comb

n=int(input())
a=[]
for i in range(n):
    a.append(list(input()))
cnt=0
for i in range(n):
    dem=a[i].count('C')
    cnt+=comb(dem,2)
for i in range(n):
    dem=0
    for j in range(n):
        if a[j][i]=='C': dem+=1
    cnt+=comb(dem,2)
print(cnt)

'''
4
CC..
C..C
.CC.
.CC.
'''