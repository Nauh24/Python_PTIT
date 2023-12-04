for t in range(int(input())):
    a,b=map(int,input().split())
    d=[0]*10
    for i in range(a,b+1):
        for j in str(i):
            d[int(j)]+=1
    print(*d)

'''
3
1 9
10 456
123 2437
'''