import math


class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,o):
        return math.sqrt((self.x-o.x)**2+(self.y-o.y)**2)

class Triangle:

    def __init__(self,p1,p2,p3):
        self.p1=p1
        self.p2=p2
        self.p3=p3
    def out(self):
        a = p1.distance(p2)
        b = p1.distance(p3)
        c = p2.distance(p3)
        if a + b > c and a + c > b and b + c > a:
            return '{:.2f}'.format(0.25 * math.sqrt((a + b + c) * (a + b - c) * (a-b+c) * (-a+b+c)))
        else:
            return 'INVALID'

a=[]
t=int(input())
for x in range(t):
    a+=[float(i) for i in input().split()]
i=0
for index in range(t):
    p1=Point(a[i],a[i+1])
    p2=Point(a[i+2],a[i+3])
    p3=Point(a[i+4],a[i+5])
    tri=Triangle(p1,p2,p3)
    print(tri.out())
    i+=6
"""
3
0 0 0 5 0 199
1 1 1 1 1 1
0 0 0 5 5 0
"""