class Matrix:

    def __init__(self,n,m,mt):
        self.n=n
        self.m=m
        self.mt=mt
    def mul(self):
        ans=[]
        for i in range(self.n):
            ans+=[[0]*self.n]
            for j in range(self.n):
                for k in range(self.m):
                    ans[i][j]+=self.mt[i][k]*self.mt[j][k]
        return Matrix(self.n,self.m,ans)

    def __str__(self):
        for i in self.mt:
            print(*i)
        return ''

for t in range(int(input())):
    n,m=map(int,input().split())
    mt=[]
    for i in range(n):
        mt.append([int(j) for j in input().split()])
    a=Matrix(n,m,mt)
    print(a.mul())
"""
1
2  2
1  2
3  4
"""