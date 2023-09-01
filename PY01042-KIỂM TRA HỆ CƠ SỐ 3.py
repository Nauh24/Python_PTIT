def solve(s):
    for i in s:
        if i!='0' and i!='1' and i!='2':
            return 'NO'
    return 'YES'
for t in range(int(input())):
    s=input()
    print(solve(s))
