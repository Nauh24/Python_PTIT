def check(a,n):
    for i in range(2,n+1):
        if a%i==0:
            return False
    return True
while True:
    str = input()
    if str=="-1":
        break
    a,b=map(int,str.split())
    n=int(input())
    cnt=0
    for i in range(a,b+1):
        if check(i,n): cnt+=1
    print(cnt)