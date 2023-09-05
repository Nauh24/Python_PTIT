
s=input()
n=len(s)
vs=[0]*n
def Try(res):
    if len(res)==n:
        print(res)
        return
    for i in range(n):
        if vs[i]==0:
            vs[i]=1
            Try(res+s[i])
            vs[i]=0
Try('')