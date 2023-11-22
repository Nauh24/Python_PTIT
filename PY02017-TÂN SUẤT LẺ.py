
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    #0.75s
    '''
    b=set(a)
    for i in b:
    if a.count(i)%2==1:
        print(i)
        break
    '''
    #0.07s
    ans=a[0]
    for i in a[1:]:
        ans^=i
        print(ans)
    print(ans)

'''
2
7
1 2 3 2 3 1 3
5
1 1 3 3 2
'''