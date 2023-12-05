def check(s):
    return s==s[::-1]
file=open('VANBAN.in','r')
d={}
a=[]
for i in file:
    a+=list(i.split())
Max=0
for i in a:
    if len(i)>=Max and check(i):
        Max=len(i)
b=[]
for i in a:
    if len(i)==Max and check(i) and i not in b:
        print(i+' ',a.count(i))
        b.append(i)
