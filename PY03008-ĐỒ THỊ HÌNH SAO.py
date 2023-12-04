n=int(input())
d={}
for i in range(n-1):
    a=list(map(int,input().split()))
    for j in a:
        if j not in d:
            d[j]=1
        else:
            d[j]+=1
ok=False
for i in d:
    #print(i,d[i])
    if d[i]>1 and d[i]!=n-1:
        break
    elif d[i]==n-1:
        ok=True
if ok:
    print('Yes')
else: print('No')
    
'''
5
1 2
1 3
1 4
1 5
'''