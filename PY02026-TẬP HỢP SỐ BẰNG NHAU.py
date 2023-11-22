n,m=map(int,input().split())
a=sorted(set(map(int,input().split())))
b=sorted(set(map(int,input().split())))
if a==b:
    print('YES')
else:
    print('NO')

'''
12 18
1 2 3 4 5 1 2 3 5 4 1 2
1 1 1 1 1 1 1 1 1 2 3 4 5 5 5 5 5 5
'''