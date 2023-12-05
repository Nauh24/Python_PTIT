for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    cnt=0
    for i in range(n-1):
        Max=max(a[i],a[i+1])
        Min=min(a[i],a[i+1])
        while Max>2*Min:
            cnt+=1
            Min*=2
    print(cnt)

'''
6
4
4 2 10 1
2
1 3
2
6 1
3
1 4 2
5
1 2 3 4 3
12
4 31 25 50 30 20 34 46 42 16 15 16
'''
