s=input()
ok=True
while len(s)>0:
    if s[:3]=='688':
       s=s[3:]
    elif s[:2]=='68':
       s=s[2:]
    elif s[:1]=='6':
        s=s[1:]
    else:
        ok=False
        break
if ok: print('YES')
else: print('NO')