MAX =10**18
a =[]
i=1
while i<=MAX:
    j=1
    while j<=MAX:
        k=1
        while k<=MAX:
            a.append(i*j*k)
            k*=5
        j*=3
    i*=2
a.sort()
def binSearch(l,r,x):
    if l>r:
        return 'Not in sequence'
    m=(l+r)//2
    if a[m]==x:
        return m+1
    if a[m]<x:
        return binSearch(m+1,r,x)
    return binSearch(l,m-1,x)
for t in range(int(input())):
    n=int(input())
    print(binSearch(0,len(a),n))