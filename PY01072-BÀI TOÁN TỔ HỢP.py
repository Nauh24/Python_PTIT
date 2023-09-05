
n,k=map(int,input().split())
a=list(map(int,input().split()))
arr =sorted(list(set(a)))
"""for i in arr:
    print(i,end=' ')"""
n=len(arr)
b=[]

def Try(i):
    if len(b)==k:
        for j in b:
            print(j,end=' ')
        print()
    for j in range(i,n):
        b.append(arr[j])
        Try(j+1)
        b.pop()
Try(0)
