def check(n,k,u,v,ke):
    q,vs=[u],[0]*(n+1)
    vs[u]=1
    while len(q)>0:
        x=q.pop()
        if x==v: return False
        for i in ke[x]:
            if vs[i]==0 and i!=k:
                q.append(i)
                vs[i]=1
    return True 
for t in range(int(input())):
    n,m,u,v=map(int,input().split())
    ke=[]
    for i in range(n+1):
        ke.append([])
    for i in range(m):
        x,y=map(int,input().split())
        ke[x].append(y)
    cnt=0
    for i in range(1,n+1):
        if i!=u and i!=v:
            if check(n,i,u,v,ke): cnt+=1
    print(cnt)
'''
2
5 7 1 3
1 2
2 4
2 5
3 1
3 2
4 3
5 4
4 5 1 4
1 2
1 3
2 3
2 4
3 4
'''