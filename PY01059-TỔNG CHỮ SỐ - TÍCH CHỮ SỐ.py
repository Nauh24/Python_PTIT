
for t in range(int(input())):
    s=input()
    tong=0
    tich=1
    ok=0
    for i in range(len(s)):
        if i%2==0:
            tong+=int(s[i])
        else:
            if s[i]!='0':
                ok=1
                tich*=int(s[i])
    if ok==0: tich=0
    print(tong,tich,end=' ')
    print()