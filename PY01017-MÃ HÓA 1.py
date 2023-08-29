for t in range(int(input())):
    s=input()
    cnt=1
    res=''
    l=len(s)
    for i in range(1,len(s)):
        if(s[i]!=s[i-1]):
            res+=str(cnt)+str(s[i-1])
            cnt=1
        else:
            cnt+=1
    res+=str(cnt)+str(s[l-1])

    print(res)
    print()