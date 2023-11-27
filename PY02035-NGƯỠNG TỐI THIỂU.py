s=input()
k=int(input())
a=[]
b=[]
for i in range(len(s)):
    if len(s)<2: break
    ans=s[:2]
    s=s[2:]
    a.append(ans)
    if ans not in b:
        b.append(ans)
ok=False
b.sort()
for i in b:
    if a.count(i)>=k:
        print(i,a.count(i),end=' ')
        ok=True
        print()
if not ok: print('NOT FOUND')

'''
124356141111434356149
2
'''