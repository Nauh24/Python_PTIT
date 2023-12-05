file =open('CONTACT.in','r')
a=set()
for i in file:
    a.add(i.lower().strip())
a=sorted(a)
print('\n'.join(a))