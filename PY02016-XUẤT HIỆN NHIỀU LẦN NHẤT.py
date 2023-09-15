
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    MAX=a[0]
    d={}
    cnt=1
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
        if d[i]>cnt:
            MAX=i
            cnt=d[i]
    if cnt*2>len(a):
        print(MAX)
    else: print('NO')

