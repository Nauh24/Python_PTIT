for t in range(int(input())):
    n=int(input())
    a=[]
    m=n
    while n>0:
        x,y=map(int,input().split())
        a.append((x,y))
        n-=1
    a.sort(key=lambda x: x[1])
    cnt=1
    endPoint=a[0][1]
    for i in range(1,m):
        if a[i][0]>=endPoint:
            cnt+=1
            endPoint=a[i][1]
    print(cnt)
    

'''
1
10
39 55
37 74
0 1
19 25
65 76
51 52
19 21
5 94
46 65
32 40
'''