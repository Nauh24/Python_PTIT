
s1=input().lower()
s2=input().lower()
a=set(s1.split())
b=set(s2.split())
inter=sorted(a.intersection(b))
uni =sorted(a.union(b))

print(*uni)
print(*inter)
'''
Lap trinh huong doi tuong
Ngon ngu lap trinh C++
'''
