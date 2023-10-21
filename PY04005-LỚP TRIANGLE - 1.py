import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def doDaiCanh(self,o):
        return math.sqrt((self.x-o.x)**2+(self.y-o.y)**2)
class Triangle:

    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def Perimeter(self):
        d1=self.a.doDaiCanh(self.b)
        d2=self.a.doDaiCanh(self.c)
        d3=self.b.doDaiCanh(self.c)
        if d1+d2>d3 and d1+d3>d2 and d2+d3>d1:
            return '{:.3f}'.format(d1+d2+d3)
        else:return 'INVALID'
a = []
t = int(input())
for x in range(t):
    a += [float(i) for i in input().split()]
i = 0
for index in range(t):
    p1=Point(a[i],a[i+1])
    p2=Point(a[i+2],a[i+3])
    p3=Point(a[i+4],a[i+5])

    triagle = Triangle(p1,p2,p3)
    print(triagle.Perimeter())
    i += 6

"""
3
0 0 0 5 0 199
1 1 1 1 1 1
0 0 0 5 5 0
"""