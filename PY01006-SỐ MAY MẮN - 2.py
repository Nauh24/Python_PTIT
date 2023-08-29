for t in range(int(input())):
    s=input()
    ok=1
    for i in range(len(s)):
        if s[i]!='4'and s[i]!='7':
            ok=0
            break
    if ok==1: print('YES')
    else: print('NO')