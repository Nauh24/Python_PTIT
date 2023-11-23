
s=input()
a=[]
b=[]
for i in range(0,len(s),2):
    ans=s[:2]
    s=s[2:]
    if len(ans)==1: continue
    b.append(int(ans))
   # print(ans)
b=sorted(set(b))
print(*b)
'''
124356141111434356149
'''