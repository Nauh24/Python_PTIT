def check(s):
    down=True
    for i in range(1,len(s)):
        if down and s[i]>=s[i-1]:
            down=False
        elif not down and s[i]<=s[i-1]:
            return False
    return True
for t in range(int(input())):
    s=input()
    if check(s): print('YES')
    else: print('NO')
'''
3
12342310
23342
96515678
'''