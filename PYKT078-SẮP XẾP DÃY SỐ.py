for t in range(int(input())):
    n,m=map(int,input().split())
    a=[int(i) for i in input().split()]
    am=[]
    duong=[]
    Max=max(a)
    for i in range(n):
        if a[i]==Max:
            a.insert(i,m)
            break
    for i in a:
        if i<0: am.append(i)
        else: duong.append(i)
    for i in am: print(i,end=' ')
    for i in duong: print(i,end=' ')
    print()
'''
1
5 3
-1 2 3 4 -1
'''