while True:
    a,b,c,d=map(int,input().split())
    if a==0 and b==0 and c==0 and d==0:
        break
    cnt=0
    while True:
        if a==b and b==c and c==d :
            break
        cnt+=1
        x=a
        a=abs(a-b)
        b=abs(b-c)
        c=abs(c-d)
        d = abs(d - x)

    print(cnt)