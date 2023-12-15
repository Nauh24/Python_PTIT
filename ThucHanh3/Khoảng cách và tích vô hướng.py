import math

for t in range(int(input())):
    a,b=list(map(int,input().split())),list(map(int,input().split()))
    d=0
    tich=0
    for i in range(len(a)):
        d+=abs(a[i]-b[i])**2
        tich+=a[i]*b[i]
    d=math.sqrt(d)

    print('{:.2f}'.format(d),tich,sep=' ',end='\n')

'''
3
10 40 20 30
2 4 -5 3
2 4 6 8
5 10 -15 20
1 1 
0 0
'''