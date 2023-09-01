def check(n):
    l=len(n)
    for i in range(l-1):
        if abs(int(n[i])-int(n[i+1])) !=2: return False
    return True
for t in range(int(input())):
    s=input()
    tong=sum(int(i) for i in s)
    if tong%10==0 and check(s): print('YES')
    else: print('NO')
    print()