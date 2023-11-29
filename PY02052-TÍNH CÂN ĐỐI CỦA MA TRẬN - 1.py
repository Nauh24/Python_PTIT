n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
Sum1=0
Sum2=0
k=int(input())
for i in range(n):
    for j in range(n):
        if i>j: Sum1+=a[i][j]
        if i<j: Sum2+=a[i][j]
if abs(Sum1-Sum2)<=k: print('YES')
else: print('NO')
print(abs(Sum1-Sum2))
'''
5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
5
'''