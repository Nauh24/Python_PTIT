def bfs(u):
    q=[u]
    vs[u]=1
    while len(q)>0:
        x=q.pop()
        for i in ke[x]:
            if vs[i]==0:
                q.append(i)
                vs[i]=1
n=int(input())
m=int(input())
ke=[]
for i in range(n+1):
    ke.append([])
for i in range(m):
    x,y=map(int,input().split())
    ke[x].append(y)
    ke[y].append(x)
vs=[0]*(n+1)
bfs(1)
cnt=0
for i in range(1,n+1):
    if vs[i]==1:
        cnt+=1
if cnt==n: print('NO')
else : print('YES')

'''
3
2
1 2
2 3

4
2
1 3
2 4
'''