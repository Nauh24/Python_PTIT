for t in range(int(input())):
    n,x,m=map(float,input().split())
    s=0
    k=0
    while n<=m:
        n=n+n*x/100
        k+=1
    print(k)