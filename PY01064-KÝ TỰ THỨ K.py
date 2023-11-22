def solve(n,k):
    x=2**(n-1)
    if x==k:
        return chr(ord('A')+n-1)
    elif k<x:
        return solve(n-1,k)
    else:
        return solve(n-1,k-x)

for t in range(int(input())):
    n,k=map(int,input().split())
    print(solve(n,k))