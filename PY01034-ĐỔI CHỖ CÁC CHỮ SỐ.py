for t in range(int(input())):
    a=input()
    idx=-1
    n=len(a)
    a=list(a)
    for i in range(n-2,-1,-1):
        if a[i]>a[i+1]:
            idx=i
            break
    if idx==-1:
        print(-1)
        continue
    tmp='-1'
    res=-1
    for i in range(idx+1,n):
        if a[i]<a[idx] and a[i]>tmp:
            tmp=a[i]
            res=i
    a[idx],a[res]=a[res],a[idx]
    if a[0]=='0':
        print(-1)
    else:
        print(''.join(a))
    

'''
5
354
999
100
11101
2301512
'''