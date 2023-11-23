s=input()
b=[]
for i in range(len(s)):
    ans=s[:2]
    s=s[2:]
    if len(ans)==1: continue
    if ans not in b:
        print(ans,end=' ')
        b.append(ans)