for t in range(int(input())):
    n,p=map(int,input().split())
    cnt=0
    while n>0:
        n//=p
        cnt+=n
    print(cnt)
'''
3
62  7
76  2
3  5
'''