res=[]
def Try(i,Sum,list):
    if Sum>n: return
    if Sum==n: 
        list=list.strip()
        res.append(list)
        return
    for j in range(i,0,-1):
        Try(j,Sum+j,list+str(j)+" ")
for t in range(int(input())):
    n=int(input())
    Try(n,0,"")
    print(len(res))
    for i in res:
        print('('+i+')',end=' ')
    res.clear()
    print()