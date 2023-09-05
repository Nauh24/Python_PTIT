
s=input()
while len(s)%3!=0:
    s='0'+s
res=[s[i:i+3] for i in range(0,len(s),3)]

for i in res:
    ans = (4*int(i[0]))+(2*int(i[1]))+int(i[2])
    print(ans,end='')