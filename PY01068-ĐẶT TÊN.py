from itertools import combinations

n,k=map(int,input().split())
a=sorted(set(input().split()))
res=combinations(a,k)
for i in res:
    print(' '.join(i))


'''
6 2
DONG TAY NAM BAC TAY BAC
'''