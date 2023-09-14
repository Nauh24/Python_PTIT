for t in range(int(input())):
    n=int(input())
    a={}
    cnt=0
    for i in range(n):
        x=int(input())
        if x in a:
             a[x]+=1
        else: a[x]=1
        cnt=max(cnt,a[x])
    tmp=1000

    for i in a:
        if a[i]==cnt:
            tmp=min(tmp,i)
    print(tmp)