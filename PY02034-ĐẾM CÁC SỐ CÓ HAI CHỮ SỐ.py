s=input()
b=[]
a=[]
for i in range(len(s)):
    if len(s) <2: break
    ans=s[:2]
    s=s[2:]
    a.append(ans)
    #print(ans)
    if ans not in b:
        b.append(ans)

for i in b:
    print(i,a.count(i))

