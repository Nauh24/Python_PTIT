def bfs(u):
    q=[u]
    vs[u]=1
    while len(q)>0:
        x=q.pop()
        for i in ke[x]:
            if vs[i]==0:
                q.append(i)
                vs[i]=1

n,m,k=map(int,input().split())
ke=[]
for i in range(n+1):
    ke.append([])
vs=[0]*(n+1)
for i in range(m):
    x,y=map(int,input().split())
    ke[x].append(y)
    ke[y].append(x)
bfs(k)
ok=False
for i in range(1,n+1):
    if vs[i]==0:
        print(i)
        ok=True
if not ok: print(0)

'''
6 4 2
1 3
2 3
1 2
4 5
'''