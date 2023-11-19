
d=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
n,m=map(int,input().split())
a=[[0 for i in range(m)] for j in range(n)]
for i in range(n):
    a[i]=list(map(int,input().split()))
cnt=0
st=[[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j]==-1:
            for k in range(8):
                x,y=i+d[k][0],j+d[k][1]
                if x>=0 and x<n and y>=0 and y<m and not st[x][y]:
                    cnt+=a[x][y]
                    st[x][y]=True
print(cnt)

'''
4 4
1 1 0 1
2 -1 4 5
0 0 0 0
1 0 2 1
'''