res='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for t in range(int(input())):
    n,b=map(int,input().split())
    s=""
    while n>0:
        tmp=n%b
        s=res[tmp]+s
        n//=b
    print(s)


