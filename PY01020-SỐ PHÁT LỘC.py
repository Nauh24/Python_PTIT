for t in range(int(input())):
    s=input()
    l =len(s)
    if s[l-2]=='8' and s[l-1]=='6':
        print('YES')
    else: print('NO')