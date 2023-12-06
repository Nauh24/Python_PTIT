import re
n=int(input())
a=list()
for i in range(n):
    s=input()
    x=re.findall("[0-9]+",s)
    #x=re.split("[a-zA-Z]",s)
    for j in x:
        if j!='':
            a.append(int(j))
a.sort()
for i in a:
    print(i)
'''
3
A129h
G07bxjq3
aaaaaaa4aaaa
'''