def dfs(u,j):
    vs[u]=1
    for i in ke[u]:
        if vs[i]==0 and i!=j:
            dfs(i,j)
for t  in range(int(input())):
    n,m=map(int,input().split())
    ke=[]
    for i in range(n+1):
        ke.append([])
    for i in range(m):
        x,y=map(int,input().split())
        ke[x].append(y)
        ke[y].append(x)
    
    Max=0
    d={}
    for i in range(1,n+1):
        vs=[0]*(n+1)
        vs[i]=1
        cnt=0
        for j in range(1,n+1):
            if vs[j]==0:
                cnt+=1
                dfs(j,i) 
        Max=max(Max,cnt)
        if i not in d:
            d[i]=cnt
    ok=False
    for i in d:
        if d[i]==Max and d[i]>1:
            print(i)
            ok=True
            break
    if not ok :
        print(0)

'''
2
5 5
1 2
1 3
2 3
3 4
3 5
5 7
1 2
1 3
2 3
2 5
3 4
3 5
4 5
'''
