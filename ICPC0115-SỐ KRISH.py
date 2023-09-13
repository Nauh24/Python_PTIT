def giaithua(n):
    x=1
    for i in range(1,n+1):
        x*=i
    return x
for t in range(int(input())):
    s=input()
    sum=0
    for i in s:
        sum+=giaithua(int(i))
    if int(s)==sum:
        print('Yes')
    else: print('No')
