
for t in range(int(input())):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))

    i1,i2,i3=0,0,0
    check=False
    while i1<n and i2<m and i3<k:
        if a[i1]==b[i2] and b[i2]==c[i3]:
            print(a[i1],end=' ')
            check=True
        Min=min(a[i1],min(b[i2],c[i3]))
        #print(Min)
        if a[i1]==Min: i1+=1
        if b[i2]==Min: i2+=1
        if c[i3]==Min: i3+=1
    if not check: print('NO')
    else: print()

'''
3
6 5 8
1 5 10 20 40 80
5 7 20 80 100
3 4 15 20 30 70 80 120
3 5 4
1 5 5
3 4 5 5 10
5 5 10 20
3 3 3
1 2 3
4 5 6
7 8 9
'''