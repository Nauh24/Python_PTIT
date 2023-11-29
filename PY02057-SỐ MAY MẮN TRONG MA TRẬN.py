n,m=map(int,input().split())
a=[]
Max=0
Min=10**9
for i in range(n):
    a.append(list(map(int,input().split())))
    for j in range(m):
        if a[i][j]>Max:
            Max=a[i][j]
        if a[i][j]<Min:
            Min=a[i][j]
lucky=Max-Min
ok=False
b=[]
for i in range(n):
    for j in range(m):
        if a[i][j]==lucky:
            b.append('Vi tri [{}][{}]'.format(i,j))
            ok=True

if not ok:
    print('NOT FOUND')
else:
    print(lucky)
    for i in b:
        print(i)
'''
6 4
23 21 77 10
13 13 22 14
28 67 28 23
29 77 11 67
16 51 24 21
13 25 77 77
'''