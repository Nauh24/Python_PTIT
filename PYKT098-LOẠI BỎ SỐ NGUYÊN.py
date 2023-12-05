file =open('DATA.in','r')
a=[]
for i in file:
    a+=list(i.split())
b=[]
for i in a:
    try:
        x=int(i)
        if x>2**63: b.append(i)
    except ValueError:
        b.append(i)
b.sort()
print(*b)