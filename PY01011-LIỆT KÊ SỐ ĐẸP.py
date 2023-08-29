def check(n):
    l=len(n)
    if l%2==1 or n!=n[::-1]: return False
    for i in n:
        if int(i)%2==1: return False
    return True
for t in range(int(input())):
    n=int(input())
    for i in range(22,n,2):
        if check(str(i)): print(i,end=' ')
    print()