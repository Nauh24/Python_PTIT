f=[0,1,1]
for i in range(3,93):
    f.append(f[i-1]+f[i-2])
for t in range(int(input())):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        print(f[i],end=' ')
    print()