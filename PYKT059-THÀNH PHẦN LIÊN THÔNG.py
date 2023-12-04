
# def bfs(u,vs):
#     q=[u]
#     vs[u]=1
#     while len(q)>0:
#         x=q.pop()
#         for i in ke[x]:
#             if vs[i]==0:
#                 q.append(i)
#                 vs[i]=1
# n,m,x=map(int,input().split())
# ke=[]
# vs=[0]*(n+1)
# for i in range(n+1):
#     ke.append([])
# for i in range(m):
#     x,y=map(int,input().split())
#     ke[x].append(y)
#     ke[y].append(x)
# bfs(x,vs)
# # for i in range(1,n+1):
# #     for j in ke[i]:
# #         print(j,end=' ')
# #     print()
# for i in vs:
#     print(i,end=' ')
# ok=False
# for i in range(1,n+1):
#     if vs[i]==0:
#         print(i)
#         ok=True
# Lazygarde

n, m, k = [int(x) for x in input().split()]
a = []
for i in range(n + 1):
    a.append([])
b = [0] * (n + 1)
for i in range(m) :
    x, y = [int(x) for x in input().split()]
    a[x].append(y)
    a[y].append(x)
q = []
q.append(k)
b[k] = 1
while len(q) > 0 :
    x = q.pop()
    for i in a[x] :
        if b[i] == 0 :
            q.append(i)
            b[i] = 1
for i in range(1, n + 1) :
    if b[i] == 0 :
        print(i)
'''
6 4 2
1 3
2 3
1 2
4 5
'''