s=input()
b=[]
a=[]
for i in range(len(s)):
    ans=s[:2]
    s=s[2:]
    a.append(ans)
    #print(ans)
    if len(ans)==1: continue
    if ans not in b:
        b.append(ans)

for i in b:
    print(i,a.count(i))

