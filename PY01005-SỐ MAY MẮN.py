s=input()
k=0
for i in range(len(s)):
    if s[i]=='4' or s[i]=='7':
        k+=1
if k==4 or k==7:
    print('YES')
else: print('NO')