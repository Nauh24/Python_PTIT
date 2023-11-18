class ThiSinh:
    def __init__(self,name,bd,diem):
        self.name=name
        self.bd=bd
        self.diem=diem
    def __str__(self):
        return self.name+' '+self.bd+' '+'{:.1f}'.format(self.diem)
name =input()
bd=input()
d1=float(input())
d2=float(input())
d3=float(input())
ts=ThiSinh(name,bd,d1+d2+d3)
print(ts)

"""
Nguyen Hoang Ha
11/10/2001
4.5
10.0
5.5
"""