def mul(s):
    t=1;
    for i in s:
        t*=int(i)
    return t
for t in range(int(input())):
    n=int(input())
    a=input().split()
    a.sort(key=lambda x:(mul(x),int(x)))
    print(*a)