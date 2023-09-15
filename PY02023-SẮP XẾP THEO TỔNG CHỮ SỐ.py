
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort(key=lambda x: (sum(int(i) for i in str(x)),x))
    print(*a)