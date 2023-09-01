import math
for t in range(int(input())):

    n=input()
    n2=n[::-1]
    if math.gcd(int(n),int(n2))==1:
        print('YES')
    else:
        print('NO')