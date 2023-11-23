
n,m=map(int,input().split())
a=list(map(int,input().split()))
d={}
for i in a:
    if i not in d:
        d[i]=1
    else: d[i]+=1
a.sort(key=lambda x:(-d.get(x),x))
Max=d[a[0]]
while len(a)>0 and d[a[0]]==Max:
    a.pop(0)
if len(a)==0: print('NONE')
else: print(a[0])

#for i in d:
#    print(i,end=' ')

'''
10 4
2 3 1 2 3 4 1 2 3 2

8 4
1 2 3 4 4 3 2 1
'''