import math

for t in range(int(input())):
    n=int(input())
    res='1 * '
    for i in range(2,int(math.sqrt(n))):
        cnt=0
        if n%i==0:
            while n%i==0:
                cnt+=1
                n/=i
            if cnt>0:
                 if n!=1:
                    res += str(i) + '^' + str(cnt) + ' * '
                 else:
                     res += str(i) + '^' + str(cnt)

    if n!=1: res+=str(int(n))+'^'+'1'
    print(res)
    print()
