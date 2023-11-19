n=int(input())
chan=[]
le=[]
a=list()
while len(a) != n:
        a += list(map(int, input().split()))
for i in a:
    if i%2==0:
        chan.append(i)
    else:
        le.append(i)
chan.sort()
le.sort(reverse=True)
i1,i2=0,0
for i in a:
    if i%2==0:
        print(chan[i1],end=' ')
        i1+=1
    else:
        print(le[i2],end=' ')
        i2+=1

'''
10
1 2 3 4 5 6 7 7 9 6
'''