def stn(n):
    if len(n)<2: return False
    return n==n[::-1]
n,m=map(int,input().split())
a=[]
Max=0
for i in range(n):
    a.append(list(map(int,input().split())))
    for j in range(m):
        if stn(str(a[i][j])) and a[i][j]>Max:
            Max=a[i][j]
if Max==0:
    print('NOT FOUND')
else:
    print(Max)
    for i in range(n):
        for j in range(m):
            if a[i][j]==Max:
                print('Vi tri [{}][{}]'.format(i,j))

'''
6 4
23 21 77 10
13 13 22 14
28 29 28 23
29 77 11 19
16 26 24 21
13 25 77 77
'''