import math


class PhanSo:
    def __init__(self,tu,mau):
        self.tu=tu
        self.mau=mau
    def rutGon(self):
        x=math.gcd(self.tu,self.mau)
        self.tu//=x
        self.mau//=x
    def cong(self,p):
        self.tu=self.tu*p.mau+self.mau*p.tu
        self.mau=self.mau*p.mau
        self.rutGon()
        return '{}/{}'.format(self.tu,self.mau)
a,b,c,d=map(int,input().split())
p1 =PhanSo(a,b)
p2= PhanSo(c,d)
print(p1.cong(p2))