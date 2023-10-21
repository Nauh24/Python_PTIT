import math


class Fract:

    def __init__(self,tu,mau):
        self.tu=tu
        self.mau=mau
    def rutGon(self):
        x=math.gcd(self.tu,self.mau)
        self.tu//=x
        self.mau//=x
    def add(self,o):
        self.tu=self.tu*o.mau+self.mau*o.tu
        self.mau=self.mau*o.mau
        self.rutGon()
        return '{}/{}'.format(self.tu,self.mau)

arr=input().split()
f1=Fract(int(arr[0]),int(arr[1]))
f2=Fract(int(arr[2]),int(arr[3]))
print(f1.add(f2))