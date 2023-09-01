def solve(s):
    if len(s)<3: return 'NO'
    up=True
    for i in range(1,len(s)):
        if up and s[i]<=s[i-1]:
            up=False
        elif not up and s[i]>=s[i-1]:
            return 'NO'
    return 'YES'

for t in range(int(input())):
    n=input()
    print(solve(n))
