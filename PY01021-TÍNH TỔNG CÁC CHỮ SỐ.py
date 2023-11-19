for t in range(int(input())):
    s=input()
    res=''
    tong=0
    for i in s:
        if i.isdigit():
            tong+=int(i)
        else:
            res+=i
    res=list(res)
    res.sort()
    res=''.join(res)
    print(res+str(tong))

'''
2
AC2BEW3
ACCBA10D2EW30
'''