file =open('DATA.in','r')
h=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def trans(s,b):
    ans=0
    for i in range(len(s)):
        ans+=(int(s[i])* 2**(b-1))
        b-=1
    return h[ans]
t=int(file.readline())
for i in range(t):
    b=int(file.readline())
    s=file.readline().strip()
    if b==2:
        print(s)
        continue
    if b==4:
        b=2
    if b==8:
        b=3
    if b==16:
        b=4

    while (len(s)) %b !=0: s='0'+s
    res=[s[i:i+b] for i in range(0,len(s),b)]
    ans=''
    for i in res:
        print(trans(i,b),end='')

    print()