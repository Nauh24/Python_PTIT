for t in range(int(input())):
    p,q=input().split()
    s=input().split()
    if len(s)>1:
        x1,x2=s
    else:
        x1=s[0]
        x2=input()
    X1=int(x1.replace(p,q))+int(x2.replace(p,q))
    X2=int(x1.replace(q,p))+int(x2.replace(q,p))
    print(min(X1,X2),max(X1,X2),end=' ')
    print()
