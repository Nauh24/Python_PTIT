n,m=map(int,input().split())
c=[]
idx=0
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
N=n
M=m
if n>m:
    while n>m:
       c.append(idx)
       idx+=2
       n-=1
    for i in range(N):
        if i not in c:
            for j in range(M):
                print(a[i][j],end=' ')
            print()
elif m>n:
    while m > n:
        c.append(idx + 1)
        idx += 2
        m -= 1
    for i in range(N):
        for j in range(M):
            if j not in c:
                print(a[i][j],end=' ')
        print()

else:
    for i in range(n):
        for j in range(m):
            print(a[i][j],end=' ')
        print()


#print(*c)

'''
6 4
2 8 7 6
6 3 2 6
7 2 2 8
9 9 9 8
9 6 6 3
7 7 4 9

4 6
2 8 7 6 4 3
6 3 2 6 7 2
7 2 2 8 9 1
9 9 9 8 0 7
'''