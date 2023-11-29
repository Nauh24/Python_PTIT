n=int(input())
a=list(map(int,input().split()))
a.sort()
Max=max(a[0]*a[1],max(a[-1]*a[-2],max(a[0]*a[1]*a[-1],a[-1]*a[-2]*a[-3])))
print(Max)

'''
6
5 10 -2 3 5 2
'''