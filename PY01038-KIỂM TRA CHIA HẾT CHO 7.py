for t in range(int(input())):
    n=int(input())
    ok=0
    for i in range(1000):

        if n%7==0:
            print(n)
            ok=1
            break
        n += int(str(n)[::-1])
    if ok==0: print(-1)
    print()